import requests
from shapely.geometry import Point, Polygon, LineString
from tqdm import tqdm
import logging
from typing import List, Dict, Tuple, Optional
import importlib.resources as pkg_resources
from functools import lru_cache
import time

class OSMSearchPlus:
    def __init__(self):
        """Initialize OSM Search Plus with default settings"""
        self.api_url = 'http://overpass-api.de/api/interpreter'
        self.api_timeout = 60
        self.mode = 'radius'
        self.show_logs = False
        self.show_progress = True
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.WARNING)  # Default to WARNING
        self.tags = self._load_default_tags()
        self.node_cache = {}  # Cache for node coordinates

    def _build_query(self, tag_str: str, **kwargs) -> str:
        """Build optimized OSM query"""
        # Basic query structure without memory limits
        query = f"""
        [out:json][timeout:{self.api_timeout}];
        ("""
        
        if self.mode == 'radius':
            query += f"""
            node{tag_str}(around:{kwargs['radius']},{kwargs['lat']},{kwargs['lon']});
            way{tag_str}(around:{kwargs['radius']},{kwargs['lat']},{kwargs['lon']});
            relation{tag_str}(around:{kwargs['radius']},{kwargs['lat']},{kwargs['lon']});
            """
        elif self.mode == 'bbox':
            query += f"""
            node{tag_str}({kwargs['min_lat']},{kwargs['min_lon']},{kwargs['max_lat']},{kwargs['max_lon']});
            way{tag_str}({kwargs['min_lat']},{kwargs['min_lon']},{kwargs['max_lat']},{kwargs['max_lon']});
            relation{tag_str}({kwargs['min_lat']},{kwargs['min_lon']},{kwargs['max_lat']},{kwargs['max_lon']});
            """
        elif self.mode == 'polygon':
            points_str = " ".join(f"{lat} {lon}" for lat, lon in kwargs['polygon_coords'])
            query += f"""
            node{tag_str}(poly:"{points_str}");
            way{tag_str}(poly:"{points_str}");
            relation{tag_str}(poly:"{points_str}");
            """

        query += """
        );
        out body;
        >;
        out skel qt;
        """
        
        if self.show_logs:
            self.logger.debug(f"Generated query:\n{query}")
        
        return query.strip()

    def _query_api(self, query: str, max_retries: int = 5, timeout: int = 180) -> Dict:
        """Query Overpass API directly with retries and better timeout handling"""
        for attempt in range(max_retries):
            try:
                if self.show_logs:
                    self.logger.debug(f"Sending API request (attempt {attempt + 1}/{max_retries})...")
                
                response = requests.post(
                    self.api_url, 
                    data={'data': query},
                    timeout=timeout  # Increased to 3 minutes
                )
                
                if self.show_logs:
                    self.logger.debug(f"API response status: {response.status_code}")
                
                response.raise_for_status()
                data = response.json()
                
                if 'remark' in data and self.show_logs:
                    self.logger.warning(f"API warning: {data['remark']}")
                    if 'rate_limited' in str(data['remark']).lower():
                        if attempt < max_retries - 1:
                            wait_time = min(5 ** attempt, 300)  # Longer exponential backoff, max 5 minutes
                            self.logger.info(f"Rate limited. Waiting {wait_time} seconds...")
                            time.sleep(wait_time)
                            continue
                
                return data
                
            except requests.exceptions.Timeout:
                if attempt < max_retries - 1:
                    wait_time = min(5 ** attempt, 300)  # Longer wait times between retries
                    self.logger.warning(f"Request timed out. Retrying in {wait_time} seconds...")
                    time.sleep(wait_time)
                    continue
                else:
                    self.logger.error("All retry attempts failed due to timeout")
                    raise
                
            except requests.exceptions.RequestException as e:
                self.logger.error(f"API request failed: {e}")
                raise

    def _process_results(self, data: Dict) -> List[Dict]:
        """Process API results with node caching"""
        found_elements = []
        
        # First, cache all nodes
        for element in data.get('elements', []):
            if element['type'] == 'node':
                self.node_cache[element['id']] = (element['lat'], element['lon'])
        
        # Process elements
        for element in data.get('elements', []):
            if element['type'] == 'node':
                found_elements.append({
                    'type': 'node',
                    'id': element['id'],
                    'lat': element['lat'],
                    'lon': element['lon'],
                    'tags': element.get('tags', {})
                })
            elif element['type'] == 'way':
                # Get center point from cached nodes
                nodes = []
                for node_id in element.get('nodes', []):
                    if node_id in self.node_cache:
                        nodes.append(self.node_cache[node_id])
                
                if nodes:
                    found_elements.append({
                        'type': 'way',
                        'id': element['id'],
                        'nodes': nodes,
                        'tags': element.get('tags', {})
                    })
        
        return found_elements

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
            self.logger.setLevel(logging.INFO if show_logs else logging.WARNING)
        if show_progress is not None:
            self.show_progress = show_progress

        if self.show_logs:
            self.logger.info(f"Starting search in {self.mode} mode")

        # Get missing parameters interactively
        params = self._get_missing_params(locals())
        
        # Convert radius to meters if needed
        if params.get('radius'):
            params['radius'] *= 1609.34

        try:
            with tqdm(total=100, disable=not self.show_progress) as pbar:
                all_elements = []
                total_tags = len(self.tags)
                
                # Process one tag at a time
                for i, (key, value) in enumerate(self.tags.items()):
                    if self.show_logs:
                        self.logger.info(f"Processing tag {i+1}/{total_tags}: {key}={value}")
                    
                    # Build single tag query
                    tag_str = f'["{key}"="{value}"]'
                    
                    # Execute query for this tag
                    query = self._build_query(tag_str, **params)
                    if self.show_logs:
                        self.logger.debug(f"Executing query: {query}")
                    
                    try:
                        result = self._query_api(query)
                        elements = self._process_results(result)
                        all_elements.extend(elements)
                        if self.show_logs:
                            self.logger.info(f"Found {len(elements)} elements for tag {key}")
                    except Exception as e:
                        if self.show_logs:
                            self.logger.warning(f"Query failed for tag {key}: {str(e)}")
                        continue
                    
                    pbar.update(100 // total_tags)
                
                # Remove duplicates
                if self.show_logs:
                    self.logger.info(f"Found {len(all_elements)} total elements before deduplication")
                
                seen = set()
                unique_elements = []
                for elem in all_elements:
                    elem_id = (elem['type'], elem['id'])
                    if elem_id not in seen:
                        seen.add(elem_id)
                        unique_elements.append(elem)
                
                if self.show_logs:
                    self.logger.info(f"Returning {len(unique_elements)} unique elements")
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

    def _get_polygon_params(self, provided: Dict) -> Dict:
        """Get or validate polygon search parameters"""
        params = {}
        if provided['polygon_coords'] is None:
            print("\n🌍 Polygon Search Setup:")
            print("Enter polygon coordinates (lat,lon), one point per line.")
            print("Enter empty line when done.")
            points = []
            while True:
                point = input("Enter point (lat,lon) or press Enter to finish: ")
                if not point:
                    break
                lat, lon = map(float, point.split(','))
                assert self._validate_coordinates(lat, lon), f"Invalid coordinates: {lat}, {lon}"
                points.append((lat, lon))
            if len(points) < 3:
                raise ValueError("Polygon needs at least 3 points")
            # Close the polygon if needed
            if points[0] != points[-1]:
                points.append(points[0])
            params['polygon_coords'] = points
        else:
            params['polygon_coords'] = provided['polygon_coords']
        return params

    def _get_bbox_params(self, provided: Dict) -> Dict:
        """Get or validate bbox search parameters"""
        params = {}
        if None in (provided['min_lat'], provided['min_lon'], provided['max_lat'], provided['max_lon']):
            print("\n🌍 Bounding Box Search Setup:")
            params['min_lat'] = provided['min_lat'] if provided['min_lat'] is not None else float(input("Enter minimum latitude (South boundary): "))
            params['min_lon'] = provided['min_lon'] if provided['min_lon'] is not None else float(input("Enter minimum longitude (West boundary): "))
            params['max_lat'] = provided['max_lat'] if provided['max_lat'] is not None else float(input("Enter maximum latitude (North boundary): "))
            params['max_lon'] = provided['max_lon'] if provided['max_lon'] is not None else float(input("Enter maximum longitude (East boundary): "))
        else:
            params.update({
                'min_lat': provided['min_lat'],
                'min_lon': provided['min_lon'],
                'max_lat': provided['max_lat'],
                'max_lon': provided['max_lon']
            })
        
        # Validate coordinates
        for lat in [params['min_lat'], params['max_lat']]:
            for lon in [params['min_lon'], params['max_lon']]:
                assert self._validate_coordinates(lat, lon), f"Invalid coordinates: {lat}, {lon}"
        
        # Ensure min/max are correct
        if params['min_lat'] > params['max_lat']:
            params['min_lat'], params['max_lat'] = params['max_lat'], params['min_lat']
        if params['min_lon'] > params['max_lon']:
            params['min_lon'], params['max_lon'] = params['max_lon'], params['min_lon']
            
        return params

    def _execute_chunk(self, params: Dict, tag_str: str, all_elements: List, pbar: tqdm, chunk_index: int, total_chunks: int):
        """Execute a single chunk of the search with progress tracking"""
        try:
            query = self._build_query(tag_str, **params)
            self.logger.debug(f"Executing query: {query}")
            
            result = self._query_api(query)
            self.logger.info(f"API response received with {len(result.get('elements', []))} elements")
            
            elements = self._process_results(result)
            self.logger.info(f"Processed {len(elements)} elements from chunk {chunk_index + 1}")
            
            all_elements.extend(elements)
            pbar.update(100 // total_chunks)
            
        except Exception as e:
            self.logger.error(f"Error in chunk {chunk_index + 1}: {str(e)}", exc_info=True)
            raise

    def _split_polygon(self, polygon: Polygon, max_area: float = 0.1) -> List[List[Tuple[float, float]]]:
        """Split polygon into smaller chunks if too large"""
        if polygon.area <= max_area:
            return [list(polygon.exterior.coords)]
        
        minx, miny, maxx, maxy = polygon.bounds
        chunks = max(1, int(polygon.area / max_area))
        chunk_size = (maxx - minx) / chunks
        
        chunk_polygons = []
        for i in range(chunks):
            for j in range(chunks):
                x1 = minx + (i * chunk_size)
                y1 = miny + (j * chunk_size)
                x2 = x1 + chunk_size
                y2 = y1 + chunk_size
                chunk = Polygon([(x1, y1), (x2, y1), (x2, y2), (x1, y2), (x1, y1)])
                if polygon.intersects(chunk):
                    intersection = polygon.intersection(chunk)
                    if not intersection.is_empty:
                        chunk_polygons.append(list(intersection.exterior.coords))
        return chunk_polygons

    def _split_bbox(self, params: Dict) -> List[Dict]:
        """Split bbox into smaller chunks if too large"""
        lat_diff = abs(params['max_lat'] - params['min_lat'])
        lon_diff = abs(params['max_lon'] - params['min_lon'])
        area = lat_diff * lon_diff
        
        if area <= 0.1:
            return [params]
        
        chunks = max(1, int(area / 0.1))
        chunk_size_lat = lat_diff / chunks
        chunk_size_lon = lon_diff / chunks
        
        chunk_params = []
        for i in range(chunks):
            for j in range(chunks):
                chunk = {
                    'min_lat': params['min_lat'] + (i * chunk_size_lat),
                    'max_lat': params['min_lat'] + ((i + 1) * chunk_size_lat),
                    'min_lon': params['min_lon'] + (j * chunk_size_lon),
                    'max_lon': params['min_lon'] + ((j + 1) * chunk_size_lon)
                }
                chunk_params.append(chunk)
        return chunk_params

    # Similar optimized methods for _get_polygon_params and _get_bbox_params... 