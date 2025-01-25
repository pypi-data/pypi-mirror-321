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

@dataclass
class LocationResult:
    """Data class to store search results"""
    name: str
    latitude: float
    longitude: float
    distance: Optional[float]
    tags: Dict[str, str]
    osm_id: str
    type: str
    elevation: Optional[float] = None
    owner: Optional[str] = None  # Property owner
    owner_type: Optional[str] = None  # private, public, military, etc.
    parcel_id: Optional[str] = None  # Property parcel ID
    google_maps_url: Optional[str] = None
    bing_maps_url: Optional[str] = None
    description: Optional[str] = None
    condition: Optional[str] = None
    access_info: Optional[str] = None
    historical_info: Optional[str] = None

    def __post_init__(self):
        """Generate map URLs after initialization"""
        # Google Maps URL with marker and zoom level 18 (very close)
        self.google_maps_url = f"https://www.google.com/maps?q={self.latitude},{self.longitude}&z=18"
        # Bing Maps URL with aerial view and zoom level 18
        self.bing_maps_url = f"https://www.bing.com/maps?cp={self.latitude}~{self.longitude}&style=h&lvl=18"

class OSMSearchPlus:
    def __init__(self, logger=None):
        """Initialize OSM searcher with optional custom logger"""
        self.api_url = 'https://overpass-api.de/api/interpreter'
        self.elevation_api = 'https://api.open-elevation.com/api/v1/lookup'
        self.massgis_api = 'https://arcgisserver.digital.mass.gov/MassGIS/ParcelByPoint'
        self.timeout = 60
        self.logger = logger or self._setup_default_logger()
        self.geolocator = Nominatim(user_agent="autobex")
        
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
        
        # Try to get name from tags
        if 'name' in tags:
            name_parts.append(tags['name'])
        else:
            # Try reverse geocoding
            try:
                location = self.geolocator.reverse(f"{lat}, {lon}", language="en")
                if location and location.address:
                    address_parts = location.address.split(", ")[:2]
                    name_parts.append(", ".join(address_parts))
            except Exception as e:
                self.logger.error(f"Geocoding error: {e}")
        
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

    def get_property_info(self, lat: float, lon: float) -> Tuple[Optional[str], Optional[str], Optional[str]]:
        """Get property ownership information from MassGIS"""
        try:
            response = requests.get(
                self.massgis_api,
                params={
                    'X': lon,  # GIS systems often use lon,lat order
                    'Y': lat,
                    'FORMAT': 'json'
                },
                timeout=self.timeout
            )
            response.raise_for_status()
            data = response.json()
            
            if data and 'features' in data and data['features']:
                feature = data['features'][0]
                props = feature['properties']
                return (
                    props.get('OWNER_NAME'),
                    props.get('OWNER_TYPE'),  # e.g., PUBLIC, PRIVATE, MIXED
                    props.get('MAP_PAR_ID')   # parcel ID
                )
            return None, None, None
            
        except Exception as e:
            self.logger.debug(f"Failed to get property info: {e}")
            return None, None, None

    def search(self, lat: float = None, lon: float = None, radius: float = None,
              polygon_coords: List[Tuple[float, float]] = None,
              show_logs: bool = False, group_distance: float = 300) -> List[List[LocationResult]]:
        """
        Search for abandoned places using either radius or polygon search
        
        Args:
            lat: Center latitude for radius search
            lon: Center longitude for radius search
            radius: Search radius in miles
            polygon_coords: List of (lat,lon) points defining search polygon
            show_logs: Show detailed logs
            group_distance: Maximum distance in meters between locations in same group
        """
        if polygon_coords:
            if show_logs:
                self.logger.info("\nSearching in polygon area")
        else:
            if not all([lat, lon, radius]):
                raise ValueError("Must provide either polygon_coords or (lat, lon, radius)")
            if show_logs:
                self.logger.info(f"\nSearching at {lat}, {lon} with {radius} mile radius")

        if show_logs:
            self.logger.info("\nUsing tags:")
            for tag in self.tags:
                self.logger.info(f"  • {tag}")

        # Convert radius to meters for API
        radius_meters = int(radius * 1609.34) if radius else None
        results = []
        node_cache = {}

        try:
            for tag in self.tags:
                if show_logs:
                    self.logger.info(f"\nQuerying for tag: {tag}")

                tag_parts = tag.split('=', 1)
                tag_key = tag_parts[0]
                tag_value = tag_parts[1] if len(tag_parts) > 1 else None

                # Build area filter based on search type
                if polygon_coords:
                    # Format points for Overpass API: lat1 lon1 lat2 lon2 lat3 lon3 ...
                    points_str = " ".join(f"{lat} {lon}" for lat, lon in polygon_coords)
                    area_filter = f"(poly:'{points_str}')"
                else:
                    area_filter = f"(around:{radius_meters},{lat},{lon})"

                query = f"""
                [out:json][timeout:{self.timeout}];
                (
                  node["{tag_key}"{f'="{tag_value}"' if tag_value else ''}]{area_filter};
                  way["{tag_key}"{f'="{tag_value}"' if tag_value else ''}]{area_filter};
                );
                out body;
                >;
                out skel qt;
                """

                if show_logs:
                    self.logger.debug(f"Query:\n{query}")

                # Send request
                response = requests.post(
                    self.api_url,
                    data={'data': query},
                    timeout=self.timeout
                )
                response.raise_for_status()
                data = response.json()

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
                    owner, owner_type, parcel_id = self.get_property_info(result_lat, result_lon)
                    result = LocationResult(
                        name=self.get_location_name(result_lat, result_lon, element['tags']),
                        latitude=result_lat,
                        longitude=result_lon,
                        distance=distance,
                        tags=element['tags'],
                        osm_id=str(element['id']),
                        type=element['type'],
                        elevation=self.get_elevation(result_lat, result_lon),
                        owner=owner,
                        owner_type=owner_type,
                        parcel_id=parcel_id,
                        description=element['tags'].get('description'),
                        condition=element['tags'].get('condition'),
                        access_info=element['tags'].get('access'),
                        historical_info=element['tags'].get('historic:note')
                    )

                    # Only add if not already present
                    if not any(r.osm_id == result.osm_id for r in results):
                        results.append(result)

            # Sort results by distance
            results.sort(key=lambda x: x.distance if x.distance is not None else float('inf'))

            # Always group results
            if show_logs:
                self.logger.info("\nGrouping nearby locations...")
            return self.group_locations(results, max_distance=group_distance)

        except Exception as e:
            self.logger.error(f"Search failed: {str(e)}")
            raise 

    def group_locations(self, locations: List[LocationResult], max_distance: float = 300) -> List[List[LocationResult]]:
        """
        Group locations that are close to each other
        
        Args:
            locations: List of LocationResult objects to group
            max_distance: Maximum distance in meters between locations in same group
            
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
                    
                    # If within max_distance, add to current group
                    if dist <= max_distance:
                        current_group.add(other_idx)
                        unassigned.remove(other_idx)
                        to_check.add(other_idx)
            
            # Convert indices back to LocationResult objects and add group
            groups.append([sorted_locations[i] for i in sorted(current_group)])
        
        # Sort groups by size (largest first) and then by minimum distance
        groups.sort(key=lambda g: (-len(g), 
                    min(x.distance if x.distance is not None else float('inf') for x in g)))
        
        return groups 