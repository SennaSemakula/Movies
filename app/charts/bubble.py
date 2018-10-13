from . import graph
import doctest
import os
import plotly.graph_objs as go
import plotly

class Bubble(graph.Graph):
    """Advanced bubble graph implementation 
    
    >>> chart = Bubble([0, 1], 'Testing graph object')
    >>> chart.draw_graph([0, 2], [1, 4], [5, 8])
    [Scatter({
        'marker': {'size': [5, 8]}, 'mode': 'markers', 'x': [0, 2], 'y': [1, 4]
    })]
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
        """Generate html file that includes chart
        >>> bc.generate_file(chart_data, 'test_graph.html')
        'file:///home/dinopc/Business_Projects/Movies/app/charts/templates/test_graph.html'
        """
        graph_html = plotly.offline.plot({
                            "data": chart_data,
                            "layout": go.Layout(title=self.title)},
                            filename="templates/{}".format(filename),
                            auto_open=open_chart)

        return graph_html


#Doctests
test_data = {'x': [1, 2, 3], 'y': [2, 4, 8]}
doctest.testmod(extraglobs={
        'bc': Bubble(test_data, "Doctest Chart"),
        'path': "hello",
        'chart_data': Bubble(test_data, 'hello').draw_graph(test_data['x'], test_data['y'], [1, 2, 3]),})
