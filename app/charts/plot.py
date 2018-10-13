from . import graph
import doctest
import os
import plotly
import plotly.plotly as py
import plotly.graph_objs as go

class Plot(graph.Graph):
    """Advanced scatter plot graph implementation """
    def __init__(self, data, title):
        self.data = data
        self.title = title

    def draw_graph(self, x_axis, y_axis):
        graph_data = go.Scatter(
            x = x_axis, 
            y = y_axis,
            mode = 'markers',
            marker = dict(
                size = 20,
                color = 'rgba(152, 0, 0, .8)',
                line = dict(
                    width = 2.5,
                    color = 'rgb(0, 0, 0, 0)')))

        return [graph_data]

    def generate_file(self, chart_data, filename, open_chart=False):
        PATH = "{}/templates".format(os.getcwd())

        if os.path.isdir(PATH) is False:
            os.mkdir(PATH)

        graph_html = plotly.offline.plot({
                                "data": chart_data,
                                "layout": go.Layout(title=self.title)},
                                filename="templates/{}".format(filename),
                                auto_open=open_chart)

        return graph_html



