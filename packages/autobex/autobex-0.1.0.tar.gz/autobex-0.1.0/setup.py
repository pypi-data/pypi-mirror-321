from setuptools import setup, find_packages

long_description = """
Autobex

An enhanced OpenStreetMap search utility with multiple search modes and progress bars.

Features:
- Multiple search modes (radius, polygon, bbox)
- Progress bars for all operations
- Error handling and logging
- Type hints for better IDE support
"""

setup(
    name="autobex",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'overpy>=0.6',
        'shapely>=2.0',
        'tqdm>=4.65.0',
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="An enhanced OpenStreetMap search utility with multiple search modes and progress bars",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/autobex",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
) 