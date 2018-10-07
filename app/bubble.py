from graph import Graph
import plotly.graph_objs as go
import plotly

"""Class that will generate a simple plot chart"""
class Bubble(Graph):
    def __init__(self, data, title):
        self.data = data
        self.title = title

    def draw_graph(self, x_axis, y_axis, circ_radius):
        chart = go.Scatter(x = x_axis,y = y_axis,
                mode='markers',marker=dict(size=circ_radius,))

        data = [chart]

        return data

    def generate_file(self, chart_data, filename, open_chart=False):
        graph_html = plotly.offline.plot({
                            "data": chart_data,
                            "layout": go.Layout(title=self.title)},
                            filename="templates/{}".format(filename),
                            auto_open=open_chart)

        return graph_html
