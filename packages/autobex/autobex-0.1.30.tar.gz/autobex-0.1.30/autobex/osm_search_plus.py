import sys
print(sys.executable)
print(sys.version)
import overpy
from shapely.geometry import Point, Polygon, LineString
from tqdm import tqdm
import time
from typing import List, Dict, Union, Tuple, Optional
import logging
import os
from pathlib import Path
import importlib.resources as pkg_resources
from functools import lru_cache

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
        self.tags = self._load_default_tags()

    @staticmethod
    @lru_cache(maxsize=1)  # Cache the help text
    def help() -> str:
        """Show help information about using the searcher"""
        help_text = """
🔍 Autobex Search Modes:

1. Radius Search:
   searcher.search(
       lat=40.7580,          # Latitude
       lon=-73.9855,         # Longitude
       radius=1.5,           # Radius in miles
       mode='radius'         # Optional, default mode
   )

2. Polygon Search:
   searcher.search(
       polygon_coords=[      # List of (lat, lon) points
           (40.7829, -73.9654),  # Point 1
           (40.7829, -73.9804),  # Point 2
           (40.7641, -73.9804),  # Point 3
           (40.7641, -73.9654),  # Point 4
           (40.7829, -73.9654)   # Close polygon
       ],
       mode='polygon'
   )

3. Bounding Box Search:
   searcher.search(
       min_lat=40.7641,     # South boundary
       min_lon=-73.9804,    # West boundary
       max_lat=40.7829,     # North boundary
       max_lon=-73.9654,    # East boundary
       mode='bbox'
   )

Optional Parameters for any search:
- show_logs=True/False      # Show detailed logs
- show_progress=True/False  # Show progress bars

Example:
    from autobex import OSMSearchPlus
    searcher = OSMSearchPlus()
    results = searcher.search(lat=40.7580, lon=-73.9855, radius=1.5)
        """
        print(help_text)

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

    @staticmethod
    @lru_cache(maxsize=32)  # Cache tag parsing results
    def _parse_tags(content: str) -> Dict[str, str]:
        """Parse tags from content string"""
        return {
            line.split('=', 1)[0].strip(): line.split('=', 1)[1].strip()
            for line in content.splitlines()
            if line.strip() and not line.startswith('#')
        }

    @staticmethod
    @lru_cache(maxsize=32)  # Cache coordinate validation
    def _validate_coordinates(lat: float, lon: float) -> bool:
        """Validate latitude and longitude values"""
        return -90 <= lat <= 90 and -180 <= lon <= 180

    def _load_default_tags(self) -> Dict[str, str]:
        """Load default tags from package resources"""
        try:
            with pkg_resources.open_text('autobex', 'tags.txt') as f:
                return self._parse_tags(f.read())
        except Exception as e:
            self.logger.error(f"Error reading package tags: {str(e)}")
            raise

    def _build_query(self, tag_str: str, **kwargs) -> str:
        """Build optimized OSM query with memory limits"""
        # Add memory and timeout limits
        query_header = f"""
        [out:json][timeout:{self.api_timeout}][maxsize:512];  // Limit memory usage
        area[name="New York City"]->.searchArea;  // Limit to NYC area for testing
        ("""

        # Build optimized filters
        if self.mode == 'radius':
            # Split into smaller radius chunks
            radius_meters = kwargs['radius']
            if radius_meters > 1000:  # If radius > 1km
                radius_meters = 1000  # Limit initial search radius
            
            area_filter = f"(around:{radius_meters},{kwargs['lat']},{kwargs['lon']})"
        elif self.mode == 'bbox':
            area_filter = f"({kwargs['min_lat']},{kwargs['min_lon']},{kwargs['max_lat']},{kwargs['max_lon']})"
        else:
            area_filter = ""

        # Build query with optimized filters
        query = f"""
        {query_header}
          node{tag_str}{area_filter};
          way{tag_str}{area_filter};
        );
        out body qt;
        """

        return query

    def _process_results(self, result: overpy.Result) -> List[Dict]:
        """Process and format search results"""
        found_elements = []
        
        # Process nodes
        found_elements.extend({
            'type': 'node',
            'id': node.id,
            'lat': node.lat,
            'lon': node.lon,
            'tags': node.tags
        } for node in result.nodes)
        
        # Process ways
        found_elements.extend({
            'type': 'way',
            'id': way.id,
            'nodes': [(n.lat, n.lon) for n in way.nodes],
            'tags': way.tags
        } for way in result.ways)
        
        return found_elements

    def search(self, 
               lat: Optional[float] = None, 
               lon: Optional[float] = None, 
               radius: Optional[float] = None,
               polygon_coords: Optional[List[Tuple[float, float]]] = None,
               min_lat: Optional[float] = None, 
               min_lon: Optional[float] = None,
               max_lat: Optional[float] = None, 
               max_lon: Optional[float] = None,
               mode: Optional[str] = None,
               show_logs: Optional[bool] = None,
               show_progress: Optional[bool] = None) -> List[Dict]:
        """Search OSM with optional configuration"""
        
        # Update configuration
        if mode is not None:
            self.mode = mode.lower()
        if show_logs is not None:
            self.show_logs = show_logs
        if show_progress is not None:
            self.show_progress = show_progress

        # Get missing parameters interactively
        params = self._get_missing_params(locals())
        
        # Convert radius to meters
        if params.get('radius'):
            params['radius'] *= 1609.34

        # Build and execute query
        tag_str = ''.join(f'["{k}"="{v}"]' for k, v in self.tags.items())
        
        try:
            with tqdm(total=100, disable=not self.show_progress) as pbar:
                all_elements = []
                
                # For radius search, use pagination
                if self.mode == 'radius':
                    radius_meters = params['radius']
                    chunks = max(1, int(radius_meters / 1000))  # Split into 1km chunks
                    chunk_size = radius_meters / chunks
                    
                    for i in range(chunks):
                        current_radius = chunk_size * (i + 1)
                        params['radius'] = min(current_radius, radius_meters)
                        
                        query = self._build_query(tag_str, **params)
                        result = self.api.query(query)
                        elements = self._process_results(result)
                        all_elements.extend(elements)
                        
                        pbar.update(100 // chunks)
                else:
                    # For other modes, single query
                    query = self._build_query(tag_str, **params)
                    result = self.api.query(query)
                    all_elements = self._process_results(result)
                    pbar.update(100)
                
                # Remove duplicates by ID
                seen = set()
                unique_elements = []
                for elem in all_elements:
                    elem_id = (elem['type'], elem['id'])
                    if elem_id not in seen:
                        seen.add(elem_id)
                        unique_elements.append(elem)
                
                return unique_elements
                
        except Exception as e:
            self.logger.error(f"Error during search: {str(e)}")
            raise

    def _get_missing_params(self, provided: Dict) -> Dict:
        """Get missing parameters interactively or validate existing ones"""
        params = {}
        
        if self.mode == 'radius':
            params.update(self._get_radius_params(provided))
        elif self.mode == 'polygon':
            params.update(self._get_polygon_params(provided))
        elif self.mode == 'bbox':
            params.update(self._get_bbox_params(provided))
            
        return params

    def _get_radius_params(self, provided: Dict) -> Dict:
        """Get or validate radius search parameters"""
        params = {}
        print("\n🌍 Radius Search Setup:") if None in (provided['lat'], provided['lon'], provided['radius']) else None
        
        params['lat'] = provided['lat'] if provided['lat'] is not None else float(input("Enter latitude (e.g., 40.7580): "))
        params['lon'] = provided['lon'] if provided['lon'] is not None else float(input("Enter longitude (e.g., -73.9855): "))
        params['radius'] = provided['radius'] if provided['radius'] is not None else float(input("Enter radius in miles (e.g., 0.5): "))
        
        assert self._validate_coordinates(params['lat'], params['lon']), "Invalid coordinates"
        return params

    # Similar optimized methods for _get_polygon_params and _get_bbox_params... 