from flask import Flask
from pprint import pprint
from plot import Plot
from bubble import Bubble

"""Main application file"""
app = Flask(__name__)

@app.route('/')
def movie_index():
    return "Welcome to Movie ratings"

"""When routed, will display visualisation"""
@app.route('/viz/plot')
def movie_visualisation():
    data = {
        "data_1": [1, 2, 3, 4, 5],
        "data_2": [4, 50, 60, 12] 
    }

    graph1 = Plot(data, "Senna Viz")
    final_graph = graph1.draw_graph(data['data_1'], data['data_2'])

    return final_graph

"""Displays a bubble chart visualiastion"""
@app.route('/viz/bubble')
def bubble_visualisation():
    data = {
        "x_data": [1, 2, 3, 4],
        "y_data": [10, 11, 12, 13],
        "circle_data": [40, 60, 80, 100]
    }

    bb_chart = Bubble(data, "Bubble Visusalisation 1")
    bb_data = bb_chart.draw_graph(data['x_data'], data['y_data'], data['circle_data'])
    
    file = bb_chart.generate_file(chart_data=bb_data, filename="Bubble_viz_1", open_chart=True)

    return file

"""Main entry point for application"""
def main():
    app.run(debug=True, host='0.0.0.0')

main()

