from abc import ABC

class Map(ABC):
    """Abstract base class that will generate a map object"""
    def __init__(self, shape_file):
        self.geo_data = shapefile

    def read_map(self, shape_file):
        """Read shapefiles and converts into geodataframe object"""
        pass

    def merge_geo_data(self, csv_data, map_data):
        """Join geographical map data with specified dataset"""
        pass

    def generate_map_image(self, file_name):
        """Return canvas image of map"""
        pass
