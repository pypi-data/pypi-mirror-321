try:
    import geopy.distance
    from geopy.geocoders import Nominatim
except ImportError:
    print("Please install geopy: pip install geopy")
    raise
import requests
import logging
import os
from typing import Dict, List, Tuple, Optional, Union
from dataclasses import dataclass
from statistics import mean
import numpy as np
import time

class OSMSearchError(Exception):
    """Custom exception for OSM search errors"""
    pass

@dataclass
class LocationGroup:
    """Class to handle operations on a group of locations"""
    locations: List['LocationResult']

    def __len__(self) -> int:
        """Return number of locations in group"""
        return len(self.locations)
    
    def __iter__(self):
        """Make group iterable"""
        return iter(self.locations)
    
    def __getitem__(self, index):
        """Allow indexing into group"""
        return self.locations[index]

    def center(self) -> Tuple[float, float]:
        """Calculate the center point of the group"""
        if not self.locations:
            raise OSMSearchError("Cannot calculate center of empty group")
        return (
            mean(loc.latitude for loc in self.locations),
            mean(loc.longitude for loc in self.locations)
        )

    def distance_span(self) -> float:
        """Calculate the maximum distance between any two points in miles"""
        if len(self.locations) < 2:
            return 0.0
        max_distance = 0
        for i, loc1 in enumerate(self.locations):
            for loc2 in self.locations[i+1:]:
                dist = geopy.distance.geodesic(
                    (loc1.latitude, loc1.longitude),
                    (loc2.latitude, loc2.longitude)
                ).miles
                max_distance = max(max_distance, dist)
        return max_distance

    def filter_by_tag(self, key: str, value: Optional[str] = None) -> List['LocationResult']:
        """Filter locations by tag key and optional value"""
        if value is None:
            return [loc for loc in self.locations if key in loc.tags]
        return [loc for loc in self.locations if loc.tags.get(key) == value]

    def average_elevation(self) -> Optional[float]:
        """Calculate average elevation of the group in meters"""
        elevations = [loc.elevation for loc in self.locations if loc.elevation is not None]
        return mean(elevations) if elevations else None

@dataclass
class LocationResult:
    """Data class to store search results"""
    # Required properties
    latitude: float
    longitude: float
    osm_id: str
    type: str  # node, way, relation
    name: str  # Generated from OSM name or reverse geocoding
    tags: Dict[str, str]  # All raw tags from OSM
    
    # Optional properties with defaults
    distance: Optional[float] = None
    elevation: Optional[float] = None
    google_maps_url: Optional[str] = None
    bing_maps_url: Optional[str] = None

    def __post_init__(self):
        """Generate map URLs after initialization"""
        # Google Maps URL with marker and zoom level 21 (maximum zoom)
        self.google_maps_url = f"https://www.google.com/maps?q={self.latitude},{self.longitude}&z=21"
        # Bing Maps URL with aerial view and zoom level 20 (maximum zoom)
        self.bing_maps_url = f"https://www.bing.com/maps?cp={self.latitude}~{self.longitude}&style=h&lvl=20"
        
    def all_tags(self, include_empty: bool = False) -> str:
        """
        Get all tags in a readable format.
        Args:
            include_empty: Whether to include tags with empty values
        Returns:
            Formatted string of all tags
        """
        lines = []
        lines.append(f"\nTags for {self.name} (OSM ID: {self.osm_id}):")
        lines.append("-" * 40)
        
        # Get sorted tags for consistent output
        sorted_tags = sorted(self.tags.items())
        
        if not sorted_tags:
            lines.append("No tags found")
            return "\n".join(lines)
            
        for key, value in sorted_tags:
            if value or include_empty:
                lines.append(f"{key:20s} = {value}")
                
        return "\n".join(lines)

class OSMSearchPlus:
    def __init__(self, logger=None):
        """Initialize OSM searcher with optional custom logger"""
        self.api_url = 'https://overpass-api.de/api/interpreter'
        self.elevation_api = 'https://api.open-elevation.com/api/v1/lookup'
        self.timeout = 30  # Reduced from 60 to 30 seconds
        self.max_retries = 3
        self.retry_delay = 5  # seconds
        self.logger = logger or self._setup_default_logger()
        
        # Configure geocoder with longer timeout and proper user agent
        self.geolocator = Nominatim(
            user_agent="autobex_osm_search",
            timeout=5  # 5 second timeout
        )
        
        # Rate limiting for geocoding
        self.geocoding_delay = 1.0  # Minimum seconds between requests
        self.last_geocoding_time = 0
        
        # Load tags from file
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.tags_file = os.path.join(script_dir, 'tags.txt')
        self.tags = self._load_tags()

    def _setup_default_logger(self) -> logging.Logger:
        """Set up default logging configuration"""
        logger = logging.getLogger('autobex_osm')
        # Clear any existing handlers
        logger.handlers = []
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        # Prevent logging propagation to root logger
        logger.propagate = False
        return logger

    def _load_tags(self) -> List[str]:
        """Load tags from tags.txt file"""
        try:
            with open(self.tags_file, 'r') as f:
                return [line.strip() for line in f.readlines() 
                        if line.strip() and not line.startswith('#')]
        except Exception as e:
            self.logger.error(f"Failed to load tags: {e}")
            return []

    def get_location_name(self, lat: float, lon: float, tags: Dict[str, str]) -> str:
        """Get meaningful name for the location using tags or reverse geocoding"""
        name_parts = []
        
        # Add type description
        if any(tag in tags for tag in ['abandoned', 'ruins', 'disused']):
            name_parts.append("Abandoned")
        
        # Try to get name from tags first
        if 'name' in tags:
            name_parts.append(tags['name'])
            return " - ".join(name_parts)
            
        # Only try reverse geocoding if no name in tags
        try:
            # Respect rate limiting
            current_time = time.time()
            time_since_last = current_time - self.last_geocoding_time
            if time_since_last < self.geocoding_delay:
                time.sleep(self.geocoding_delay - time_since_last)
            
            location = self.geolocator.reverse(f"{lat}, {lon}", language="en")
            self.last_geocoding_time = time.time()
            
            if location and location.address:
                address_parts = location.address.split(", ")[:2]
                name_parts.append(", ".join(address_parts))
        except Exception as e:
            if "429" in str(e):
                self.logger.warning("Rate limit exceeded for geocoding, waiting longer...")
                time.sleep(5)  # Wait longer on rate limit
            else:
                self.logger.debug(f"Geocoding error: {e}")
        
        return " - ".join(name_parts) if name_parts else "Unknown Location"

    def calculate_distance(self, coord1: Tuple[float, float], 
                         coord2: Tuple[float, float]) -> float:
        """Calculate distance between two coordinates in meters"""
        return geopy.distance.geodesic(coord1, coord2).meters

    def get_elevation(self, lat: float, lon: float) -> Optional[float]:
        """Get elevation for coordinates using Open-Elevation API"""
        try:
            response = requests.get(
                self.elevation_api,
                params={'locations': f'{lat},{lon}'},
                timeout=self.timeout
            )
            response.raise_for_status()
            data = response.json()
            return data['results'][0]['elevation']
        except Exception as e:
            self.logger.debug(f"Failed to get elevation: {e}")
            return None

    def _parse_coordinate(self, coord_str: str) -> float:
        """
        Parse coordinate string to decimal degrees.
        Handles multiple formats:
        - Decimal degrees (e.g., "42.3601" or "-71.0589")
        - DMS format (e.g., "41°28'50.4"N" or "71°23'35.5"W")
        """
        try:
            # First try parsing as decimal
            try:
                decimal = float(coord_str)
                if -180 <= decimal <= 180:
                    return decimal
            except ValueError:
                pass

            # If not decimal, try DMS format
            # Remove spaces and convert special quotes to standard ones
            coord_str = coord_str.strip().replace('′', "'").replace('″', '"')
            
            # Extract direction (N/S/E/W)
            direction = coord_str[-1].upper()
            if direction not in 'NSEW':
                raise ValueError(f"Invalid direction: {direction}")
            
            # Remove direction and split into degrees, minutes, seconds
            parts = coord_str[:-1].replace('°', ' ').replace("'", ' ').replace('"', ' ').split()
            
            degrees = float(parts[0])
            minutes = float(parts[1]) if len(parts) > 1 else 0
            seconds = float(parts[2]) if len(parts) > 2 else 0
            
            # Convert to decimal degrees
            decimal = degrees + (minutes / 60.0) + (seconds / 3600.0)
            
            # Make negative if South or West
            if direction in 'SW':
                decimal = -decimal
                
            # Validate range
            if (direction in 'NS' and not -90 <= decimal <= 90) or \
               (direction in 'EW' and not -180 <= decimal <= 180):
                raise ValueError("Coordinate out of valid range")
                
            return decimal
            
        except Exception as e:
            raise OSMSearchError(f"Failed to parse coordinate {coord_str}: {str(e)}")

    def _validate_coordinates(self, lat: float, lon: float) -> None:
        """Validate coordinate ranges"""
        if not -90 <= lat <= 90:
            raise ValueError(f"Latitude {lat} is out of valid range (-90 to 90)")
        if not -180 <= lon <= 180:
            raise ValueError(f"Longitude {lon} is out of valid range (-180 to 180)")

    def _send_overpass_query(self, query: str) -> dict:
        """Send query to Overpass API with retry logic"""
        for attempt in range(self.max_retries):
            try:
                response = requests.post(
                    self.api_url,
                    data={'data': query},
                    timeout=self.timeout
                )
                response.raise_for_status()
                return response.json()
            except requests.Timeout:
                if attempt < self.max_retries - 1:
                    self.logger.warning(f"Timeout, retrying in {self.retry_delay} seconds...")
                    time.sleep(self.retry_delay)
                else:
                    raise OSMSearchError("Overpass API timeout after all retries")
            except requests.RequestException as e:
                if attempt < self.max_retries - 1:
                    self.logger.warning(f"Request failed, retrying in {self.retry_delay} seconds... Error: {e}")
                    time.sleep(self.retry_delay)
                else:
                    raise OSMSearchError(f"Overpass API request failed after all retries: {e}")

    def search(self, lat: Union[str, float, None] = None, 
              lon: Union[str, float, None] = None,
              radius: Optional[float] = None, 
              polygon_coords: Optional[List[Tuple[Union[str, float], Union[str, float]]]] = None,
              limit: int = 100, sort_by: str = 'distance',
              show_logs: bool = False) -> List[LocationGroup]:
        """Search for locations using either radius or polygon search"""
        # Validate required parameters
        if not polygon_coords and not all([lat, lon, radius]):
            raise ValueError("Must provide either polygon_coords or (lat, lon, radius)")

        # Validate radius if provided
        if radius is not None and radius <= 0:
            raise ValueError(f"Radius must be positive, got {radius}")

        # Convert coordinates if they're strings
        if lat is not None and lon is not None:
            if isinstance(lat, str):
                lat = self._parse_coordinate(lat)
            if isinstance(lon, str):
                lon = self._parse_coordinate(lon)
            # Validate coordinates after conversion
            self._validate_coordinates(lat, lon)
                
        # Convert and validate polygon coordinates if provided
        if polygon_coords:
            converted_polygon = []
            for p_lat, p_lon in polygon_coords:
                if isinstance(p_lat, str):
                    p_lat = self._parse_coordinate(str(p_lat))
                if isinstance(p_lon, str):
                    p_lon = self._parse_coordinate(str(p_lon))
                # Validate each polygon coordinate
                self._validate_coordinates(p_lat, p_lon)
                converted_polygon.append((p_lat, p_lon))
            polygon_coords = converted_polygon

        if polygon_coords:
            if show_logs:
                self.logger.info("\nSearching in polygon area")
        else:
            if not all([lat, lon, radius]):
                raise OSMSearchError("Must provide either polygon_coords or (lat, lon, radius)")
            if show_logs:
                self.logger.info(f"\nSearching at {lat}, {lon} with {radius} mile radius")

        # Convert radius to meters for API
        radius_meters = int(radius * 1609.34) if radius else None

        results = []
        node_cache = {}

        try:
            for tag in self.tags:
                if show_logs:
                    self.logger.info(f"\nQuerying for tag: {tag}")

                # Build area filter based on search type
                if polygon_coords:
                    # Format points for Overpass API: lat1 lon1 lat2 lon2 lat3 lon3 ...
                    points_str = " ".join(f"{lat} {lon}" for lat, lon in polygon_coords)
                    area_filter = f"(poly:'{points_str}')"
                else:
                    area_filter = f"(around:{radius_meters},{lat},{lon})"

                # Build a single query combining all tag patterns
                if '=' in tag:
                    # Exact match (e.g., building=ruins)
                    tag_key, tag_value = tag.split('=', 1)
                    query = f"""
                    [out:json][timeout:{self.timeout}];
                    (
                      node["{tag_key}"="{tag_value}"]{area_filter};
                      way["{tag_key}"="{tag_value}"]{area_filter};
                    );
                    out body;
                    >;
                    out skel qt;
                    """
                else:
                    # Simple tag (e.g., abandoned)
                    tag_key = tag.replace('"', '\\"')  # Escape quotes
                    query = f"""
                    [out:json][timeout:{self.timeout}];
                    (
                      // Match as key with any value
                      node["{tag_key}"]{area_filter};
                      way["{tag_key}"]{area_filter};
                      // Match as value in common keys
                      node["building"="{tag_key}"]{area_filter};
                      way["building"="{tag_key}"]{area_filter};
                      node["historic"="{tag_key}"]{area_filter};
                      way["historic"="{tag_key}"]{area_filter};
                    );
                    out body;
                    >;
                    out skel qt;
                    """

                if show_logs:
                    self.logger.debug(f"Query:\n{query}")
                    self.logger.info("Sending query to Overpass API...")

                # Send request
                data = self._send_overpass_query(query)

                if show_logs:
                    self.logger.info("Processing results...")

                # Cache nodes first
                for element in data.get('elements', []):
                    if element['type'] == 'node':
                        node_cache[element['id']] = (element['lat'], element['lon'])

                # Process results
                for element in data.get('elements', []):
                    if 'tags' not in element:
                        continue

                    # Get coordinates
                    if element['type'] == 'node':
                        result_lat = element['lat']
                        result_lon = element['lon']
                    elif element['type'] == 'way':
                        # Calculate center of way
                        way_nodes = [node_cache[n] for n in element['nodes'] if n in node_cache]
                        if not way_nodes:
                            continue
                        result_lat = sum(n[0] for n in way_nodes) / len(way_nodes)
                        result_lon = sum(n[1] for n in way_nodes) / len(way_nodes)
                    else:
                        continue

                    # Calculate distance
                    distance = self.calculate_distance((lat, lon), (result_lat, result_lon))

                    # Create result object
                    result = LocationResult(
                        name=self.get_location_name(result_lat, result_lon, element['tags']),
                        latitude=result_lat,
                        longitude=result_lon,
                        distance=distance,
                        tags=element['tags'],
                        osm_id=str(element['id']),
                        type=element['type'],
                        elevation=self.get_elevation(result_lat, result_lon)
                    )

                    # Only add if not already present
                    if not any(r.osm_id == result.osm_id for r in results):
                        results.append(result)

            # Sort results based on sort_by parameter
            if sort_by == 'distance':
                results.sort(key=lambda x: x.distance if x.distance is not None else float('inf'))
            elif sort_by == 'name':
                results.sort(key=lambda x: x.name)
            else:
                raise OSMSearchError(f"Invalid sort_by value: {sort_by}. Must be 'distance' or 'name'")

            # Group results with fixed 100 meter distance
            grouped_results = self.group_locations(results)
            
            # Convert to LocationGroup objects
            grouped_results = [LocationGroup(group) for group in grouped_results]

            return grouped_results

        except Exception as e:
            self.logger.error(f"Search failed: {str(e)}")
            raise 

    def group_locations(self, locations: List[LocationResult]) -> List[List[LocationResult]]:
        """
        Group locations that are within 100 meters of each other
        
        Args:
            locations: List of LocationResult objects to group
            
        Returns:
            List of location groups, where each group is a list of LocationResult objects
        """
        if not locations:
            return []
        
        # Sort locations by distance from search center
        sorted_locations = sorted(locations, 
                                key=lambda x: x.distance if x.distance is not None else float('inf'))
        
        # Initialize groups
        groups = []
        unassigned = set(range(len(sorted_locations)))
        
        while unassigned:
            # Start new group with first unassigned location
            current = min(unassigned)
            current_group = {current}
            unassigned.remove(current)
            
            # Keep track of which locations we need to check
            to_check = {current}
            
            # Keep expanding group until no more nearby locations found
            while to_check:
                check_idx = to_check.pop()
                check_loc = sorted_locations[check_idx]
                
                # Look for nearby unassigned locations
                for other_idx in list(unassigned):
                    other_loc = sorted_locations[other_idx]
                    
                    # Calculate distance between locations
                    dist = self.calculate_distance(
                        (check_loc.latitude, check_loc.longitude),
                        (other_loc.latitude, other_loc.longitude)
                    )
                    
                    # If within 100 meters, add to current group
                    if dist <= 100:  # Fixed 100 meter grouping distance
                        current_group.add(other_idx)
                        unassigned.remove(other_idx)
                        to_check.add(other_idx)
            
            # Convert indices back to LocationResult objects and add group
            groups.append([sorted_locations[i] for i in sorted(current_group)])
        
        # Sort groups by size (largest first) and then by minimum distance
        groups.sort(key=lambda g: (-len(g), 
                    min(x.distance if x.distance is not None else float('inf') for x in g)))
        
        return groups 