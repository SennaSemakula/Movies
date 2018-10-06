from graph import Graph
from bokeh.plotting import figure, output_file, show
from bokeh.resources import CDN
from bokeh.embed import file_html

"""Class that will generate a simple plot chart"""
class Plot(Graph):
	def __init__(self, data, title):
		self.data = data
		self.title = title

	def draw_graph(self, x_axis, y_axis):
		graph = figure(title=self.title, x_axis_label='x', y_axis_label='y')
		graph.line(x_axis, y_axis, legend="Temp.", line_width=2)
		show(graph)

		return self.generate_file(graph, CDN, "Movies")

	def generate_file(self, plot, cdn_import, title):
		return file_html(plot, cdn_import, title)


