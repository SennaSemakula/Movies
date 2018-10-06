from flask import Flask
from pprint import pprint
from plot import Plot

"""Main application file"""
app = Flask(__name__)

@app.route('/')
def movie_index():
	return "Welcome to Movie ratings"

"""When routed, will display visualisation"""
@app.route('/viz')
def movie_visualisation():
	data = {
		"data_1": [1, 2, 3, 4, 5],
		"data_2": [4, 50, 60, 12] 
	}

	graph1 = Plot(data, "Senna Viz")
	final_graph = graph1.draw_graph(data['data_1'], data['data_2'])

	return final_graph

"""Main entry point for application"""
def main():
	app.run(debug=True, host='0.0.0.0')

main()

