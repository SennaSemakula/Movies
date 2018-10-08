import doctest
import os
from . import graph
import plotly.graph_objs as go
import plotly

class Bubble(graph.Graph):
    PATH = "os.getcwd()".format("/templates/test_graph.html")
    """Advanced bubble chart implementation 
    
    >>> data = {'x': [1, 2, 3], 'y': [2, 4, 8]}
    >>> bc = Bubble(data, "Doctest Chart")
    >>> chart_data = bc.draw_graph(data['x'], data['y'], [2, 4, 5])
    >>> chart_html = bc.generate_file(chart_data, 'test_graph.html')
    >>> hello = print(os.getcwd())
    >>> print(chart_html)
    Bubble.PATH
    """
    def __init__(self, data, title):
        self.data = data
        self.title = title

    def draw_graph(self, x_axis, y_axis, circ_radius):
        """Draw chart data"""
        chart = go.Scatter(x = x_axis,y = y_axis,
                mode='markers',marker=dict(size=circ_radius,))

        data = [chart]

        return data

    def generate_file(self, chart_data, filename, open_chart=False):
        """Generate html file that includes chart"""
        graph_html = plotly.offline.plot({
                            "data": chart_data,
                            "layout": go.Layout(title=self.title)},
                            filename="templates/{}".format(filename),
                            auto_open=open_chart)

        return graph_html

doctest.testmod()
