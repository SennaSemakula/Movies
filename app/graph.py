from bokeh.plotting import figure, output_file, show
import json
import plotly


"""Interface simulates interface for drawing different types of graphs
	Main purpose is to generate different types of visualisations"""
class Graph():
	def __init__(self, data, title):
		self.data = data
		self.title = title
		self.start_session()

	"""Method needed to authenticate access to graph api"""
	def start_session(self):
		with open('dev_credentials.json') as f_obj:
			creds = json.load(f_obj)

		username = creds['plotly']['username']
		token = creds['plotly']['api_token']
		plotly.tools.set_credentials_file(username=username, api_key=token)

	"""Method will initialise the base of the charts"""
	def draw_graph(self, title, x_axis, y_axis, legend):
		#retrieve and store data that can be used to build graph
		# XDATA, YDATA
		# create a new plot with a title and axis labels

		#Create a figure object with title, x_axis label and y_axis label
		#figure(args = title, x_axis, y_axis)

		
		# Choose visualisation method to display data and legend
		# e.g. can add a plot line with a legend
		

		# show the results by displaying the graph
		return None
		

	"""Following method will providing existing graphs an new dataset, updating values"""
	def update_graph(data, x_axis, y_axis):
		return None

	"""Following method will delete a specified graph""" 
	def delete_graph(graph):
		return None

	def generate_html(self, file):
		return None