# OSM Search Plus

A powerful Python package for searching OpenStreetMap data with advanced features including elevation data, property information, and location grouping.

## Features

- Search OpenStreetMap data by latitude/longitude and radius
- Get elevation data for locations
- Property information lookup
- Location grouping based on distance
- Built-in Google Maps and Bing Maps URL generation
- Comprehensive location details including:
  - Name and type
  - Distance calculations
  - Property ownership information
  - Historical information
  - Access information
  - Condition status

## Installation

```bash
pip install autobex
```

## Quick Start

```python
from autobex import OSMSearchPlus

# Initialize the searcher
searcher = OSMSearchPlus()

# Search for locations (format: lat, long)
results = searcher.search(lat=42.3601, lon=-71.0589, radius=1000)  # 1km radius

# Results are grouped by proximity
for group in results:
    for location in group:
        print(f"Name: {location.name}")
        print(f"Location: {location.latitude}, {location.longitude}")
        print(f"Distance: {location.distance}m")
        print(f"Google Maps: {location.google_maps_url}")
        print("---")
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
