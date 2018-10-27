from . import maps
from os import path
import pandas
import geopandas as gpd
import matplotlib.pyplot as plt
import descartes

CURR_PATH = path.dirname(path.abspath(__file))))

class PropertyMap(Map):
    """Template to generate chlorpleth maps for property financial data"""
    def __init__(self, shape_file, csv_file):
        self.map_file = shape_file
        self.data_file = csv_file

    def read_map(map_file, csv_data):
        data = {"map_data": "", "house_data": ""}

        try:
            data['map_data'] = gpd.GeoDataFrame.from_file(shape_file)
            data['house_data'] = pandas.read_csv(csv_data, header=0)
        except FileNotFoundError as fe:
             raise(f'Unable to find the file {fe}')
        else:
            return data

    def merge_geo_data(map_obj, csv_data, map_attr, csv_attr):
        read_data = self.read_map(map_obj, csv_data)
        map_data, csv_data = read_data[0], read_data[1]

        merged_data = map_data.set_index(map_attr).join(csv_data.set_index(csv_attr))
        return merged_data

    def config_map(self, merged_data, var, var_min, var_max, fig_size, axis, colour, edge_colour):
        """Configure type of map e.g. Chloropleth"""
        vmin, vmax = var_min, var_max
        fig, ax = plt.subplots(fig_size, figsize=axis) #axis takes a tuple (x,y)
        merged_plt = merged_data.plot(column=var, cmap=colour, ax=ax, edgecolor=edge_colour)

        return merge_plt
    def generate_file(mp_plot, filename):
        path = f'{CURR_PATH}/{file_name}'
        map_image = mp_plot.savefig(path)
