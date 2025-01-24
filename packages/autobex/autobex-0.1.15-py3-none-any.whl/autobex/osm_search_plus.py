import overpy
from shapely.geometry import Point, Polygon, LineString
from tqdm import tqdm
import time
from typing import List, Dict, Union, Tuple
import logging
import os
from pathlib import Path

class OSMSearchPlus:
    def __init__(self, api_timeout: int = 60, tags_file: str = "tags.txt"):
        """
        Initialize OSM Search Plus with configurable timeout
        
        Args:
            api_timeout (int): Timeout in seconds for API requests
            tags_file (str): Path to the tags.txt file
        """
        self.api = overpy.Overpass()
        self.api.timeout = api_timeout  # Set timeout after initialization
        self.logger = logging.getLogger(__name__)
        self.tags_file = tags_file
        self.tags = self._load_tags()

    def _load_tags(self) -> Dict[str, str]:
        """
        Load tags from tags.txt file
        
        Returns:
            Dictionary of tags
        """
        tags = {}
        try:
            if not os.path.exists(self.tags_file):
                self.logger.error(f"Tags file not found: {self.tags_file}")
                raise FileNotFoundError(f"Tags file not found: {self.tags_file}")
                
            with open(self.tags_file, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        key, value = line.split('=', 1)
                        tags[key.strip()] = value.strip()
            
            if not tags:
                self.logger.warning("No tags found in tags.txt")
            
            return tags
            
        except Exception as e:
            self.logger.error(f"Error loading tags: {str(e)}")
            raise

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
        tag_str = ' and '.join([f'"{k}"="{v}"' for k, v in self.tags.items()])
        query = f"""
        [out:json][timeout:60];
        (
          node[{tag_str}](around:{radius},{lat},{lon});
          way[{tag_str}](around:{radius},{lat},{lon});
          relation[{tag_str}](around:{radius},{lat},{lon});
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