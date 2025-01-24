import sys
print(sys.executable)
print(sys.version)
import overpy
from shapely.geometry import Point, Polygon, LineString
from tqdm import tqdm
import time
from typing import List, Dict, Union, Tuple
import logging
import os
from pathlib import Path
import importlib.resources as pkg_resources

class OSMSearchPlus:
    def __init__(self):
        """Initialize OSM Search Plus with default settings"""
        self.api = overpy.Overpass()
        self.api_timeout = 60
        self.mode = 'radius'
        self.show_logs = False
        self.show_progress = True
        
        # Configure default logging
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.WARNING)
        
        # Load default tags
        try:
            with pkg_resources.open_text('autobex', 'tags.txt') as f:
                self.tags = self._parse_tags(f)
        except Exception as e:
            self.logger.error(f"Error reading package tags: {str(e)}")
            raise

    def configure(self, 
                 mode: str = None,
                 api_timeout: int = None,
                 show_logs: bool = None,
                 show_progress: bool = None,
                 tags_file: str = None):
        """
        Update searcher configuration
        
        Args:
            mode (str): Search mode ('radius', 'polygon', or 'bbox')
            api_timeout (int): Timeout in seconds for API requests
            show_logs (bool): Whether to show logging output
            show_progress (bool): Whether to show progress bars
            tags_file (str): Path to custom tags.txt file
        """
        if mode is not None:
            self.mode = mode.lower()
        if api_timeout is not None:
            self.api_timeout = api_timeout
            self.api.timeout = api_timeout
        if show_logs is not None:
            self.show_logs = show_logs
            logging.basicConfig(level=logging.INFO if show_logs else logging.WARNING)
        if show_progress is not None:
            self.show_progress = show_progress
        if tags_file is not None:
            self.load_tags(tags_file)

    def load_tags(self, tags_file: str):
        """Load tags from external file"""
        if not os.path.exists(tags_file):
            raise FileNotFoundError(f"Tags file not found: {tags_file}")
        with open(tags_file, 'r') as f:
            self.tags = self._parse_tags(f)

    def _parse_tags(self, file_obj) -> Dict[str, str]:
        """Parse tags from a file object"""
        tags = {}
        for line in file_obj:
            line = line.strip()
            if line and not line.startswith('#'):
                key, value = line.split('=', 1)
                tags[key.strip()] = value.strip()
        return tags

    def search(self, 
               lat: float = None, 
               lon: float = None, 
               radius: float = None,
               polygon_coords: List[Tuple[float, float]] = None,
               min_lat: float = None, 
               min_lon: float = None,
               max_lat: float = None, 
               max_lon: float = None,
               mode: str = None,
               show_logs: bool = None,
               show_progress: bool = None) -> List[Dict]:
        """
        Search OSM with optional configuration
        
        Args:
            lat, lon: Center coordinates for radius search
            radius: Search radius in meters
            polygon_coords: List of (lat, lon) tuples for polygon search
            min_lat, min_lon, max_lat, max_lon: Coordinates for bbox search
            mode: Search mode ('radius', 'polygon', or 'bbox')
            show_logs: Whether to show logging output
            show_progress: Whether to show progress bars
            
        Returns:
            List of found elements with their details
        """
        # Update configuration if provided
        if mode is not None:
            self.mode = mode.lower()
        if show_logs is not None:
            self.show_logs = show_logs
            logging.basicConfig(level=logging.INFO if show_logs else logging.WARNING)
        if show_progress is not None:
            self.show_progress = show_progress

        # Perform search based on mode
        if self.mode == 'radius':
            if None in (lat, lon, radius):
                raise ValueError("Radius search requires lat, lon, and radius")
            return self.search_radius(lat, lon, radius, self.show_progress)
            
        elif self.mode == 'polygon':
            if polygon_coords is None:
                raise ValueError("Polygon search requires polygon_coords")
            return self.search_polygon(polygon_coords, self.show_progress)
            
        elif self.mode == 'bbox':
            if None in (min_lat, min_lon, max_lat, max_lon):
                raise ValueError("Bbox search requires min_lat, min_lon, max_lat, max_lon")
            return self.search_bbox(min_lat, min_lon, max_lat, max_lon, self.show_progress)
            
        else:
            raise ValueError(f"Invalid search mode: {self.mode}")

    def search_radius(
        self, 
        lat: float, 
        lon: float, 
        radius: float,
        progress: bool = True
    ) -> List[Dict]:
        """
        Search for OSM elements within a radius using tags from tags.txt
        
        Args:
            lat (float): Latitude of center point
            lon (float): Longitude of center point
            radius (float): Search radius in meters
            progress (bool): Show progress bar
            
        Returns:
            List of found elements with their details
        """
        # Fix tag formatting: use '~' for AND conditions
        tag_conditions = []
        for k, v in self.tags.items():
            tag_conditions.append(f'["{k}"="{v}"]')
        tag_str = ''.join(tag_conditions)

        query = f"""
        [out:json][timeout:60];
        (
          node{tag_str}(around:{radius},{lat},{lon});
          way{tag_str}(around:{radius},{lat},{lon});
          relation{tag_str}(around:{radius},{lat},{lon});
        );
        out body;
        >;
        out skel qt;
        """
        
        try:
            with tqdm(total=100, disable=not progress, desc="Searching OSM") as pbar:
                result = self.api.query(query)
                pbar.update(50)
                
                found_elements = []
                
                # Process nodes
                for node in result.nodes:
                    found_elements.append({
                        'type': 'node',
                        'id': node.id,
                        'lat': node.lat,
                        'lon': node.lon,
                        'tags': node.tags
                    })
                
                # Process ways
                for way in result.ways:
                    found_elements.append({
                        'type': 'way',
                        'id': way.id,
                        'nodes': [(n.lat, n.lon) for n in way.nodes],
                        'tags': way.tags
                    })
                
                pbar.update(50)
                
                return found_elements
                
        except overpy.exception.OverpassTooManyRequests:
            self.logger.error("Too many requests to Overpass API")
            raise
        except Exception as e:
            self.logger.error(f"Error during OSM search: {str(e)}")
            raise

    def search_polygon(
        self,
        polygon_coords: List[Tuple[float, float]],
        progress: bool = True
    ) -> List[Dict]:
        """
        Search for OSM elements within a polygon using tags from tags.txt
        
        Args:
            polygon_coords (list): List of (lat, lon) tuples defining the polygon
            progress (bool): Show progress bar
            
        Returns:
            List of found elements with their details
        """
        polygon = Polygon(polygon_coords)
        bbox = polygon.bounds  # (minx, miny, maxx, maxy)
        
        tag_str = ' and '.join([f'"{k}"="{v}"' for k, v in self.tags.items()])
        query = f"""
        [out:json][timeout:60];
        (
          node[{tag_str}]({bbox[1]},{bbox[0]},{bbox[3]},{bbox[2]});
          way[{tag_str}]({bbox[1]},{bbox[0]},{bbox[3]},{bbox[2]});
          relation[{tag_str}]({bbox[1]},{bbox[0]},{bbox[3]},{bbox[2]});
        );
        out body;
        >;
        out skel qt;
        """
        
        try:
            with tqdm(total=100, disable=not progress, desc="Searching in polygon") as pbar:
                result = self.api.query(query)
                pbar.update(50)
                
                found_elements = []
                
                # Filter nodes within polygon
                for node in result.nodes:
                    point = Point(node.lon, node.lat)
                    if polygon.contains(point):
                        found_elements.append({
                            'type': 'node',
                            'id': node.id,
                            'lat': node.lat,
                            'lon': node.lon,
                            'tags': node.tags
                        })
                
                # Filter ways that intersect with polygon
                for way in result.ways:
                    way_coords = [(n.lon, n.lat) for n in way.nodes]
                    way_line = LineString(way_coords)
                    if polygon.intersects(way_line):
                        found_elements.append({
                            'type': 'way',
                            'id': way.id,
                            'nodes': [(n.lat, n.lon) for n in way.nodes],
                            'tags': way.tags
                        })
                
                pbar.update(50)
                return found_elements
                
        except Exception as e:
            self.logger.error(f"Error during polygon search: {str(e)}")
            raise

    def search_bbox(
        self,
        min_lat: float,
        min_lon: float,
        max_lat: float,
        max_lon: float,
        progress: bool = True
    ) -> List[Dict]:
        """
        Search for OSM elements within a bounding box using tags from tags.txt
        
        Args:
            min_lat (float): Minimum latitude
            min_lon (float): Minimum longitude
            max_lat (float): Maximum latitude
            max_lon (float): Maximum longitude
            progress (bool): Show progress bar
            
        Returns:
            List of found elements with their details
        """
        tag_str = ' and '.join([f'"{k}"="{v}"' for k, v in self.tags.items()])
        query = f"""
        [out:json][timeout:60];
        (
          node[{tag_str}]({min_lat},{min_lon},{max_lat},{max_lon});
          way[{tag_str}]({min_lat},{min_lon},{max_lat},{max_lon});
          relation[{tag_str}]({min_lat},{min_lon},{max_lat},{max_lon});
        );
        out body;
        >;
        out skel qt;
        """
        
        try:
            with tqdm(total=100, disable=not progress, desc="Searching in bbox") as pbar:
                result = self.api.query(query)
                pbar.update(50)
                
                found_elements = []
                
                for node in result.nodes:
                    found_elements.append({
                        'type': 'node',
                        'id': node.id,
                        'lat': node.lat,
                        'lon': node.lon,
                        'tags': node.tags
                    })
                
                for way in result.ways:
                    found_elements.append({
                        'type': 'way',
                        'id': way.id,
                        'nodes': [(n.lat, n.lon) for n in way.nodes],
                        'tags': way.tags    
                    })
                
                pbar.update(50)
                return found_elements
                
        except Exception as e:
            self.logger.error(f"Error during bbox search: {str(e)}")
            raise 