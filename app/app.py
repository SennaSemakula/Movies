from flask import Flask, render_template, request
from pprint import pprint
from charts import graph
from charts import bubble, plot

"""Main application file"""
app = Flask(__name__)

@app.route('/')
def movie_index():
    return "Welcome to Movie ratings"

"""When routed, will display visualisation"""
@app.route('/viz/plot/<title>')
def movie_visualisation(title):
    data = {
        "x_data": (4, 21, 5, 53),
        "y_data": (10, 11, 12, 13),
    }

    sc_chart = plot.Plot(data, title)
    sc_data = sc_chart.draw_graph(data['x_data'], data['y_data'])

    file_name = "Scatter_1.html"
    sc_chart.generate_file(chart_data=sc_data   , filename=file_name, open_chart=False)

    return render_template(file_name)

"""Displays a bubble chart visualiastion"""
@app.route('/viz/bubble/<title>')
def bubble_visualisation(title):
    data = {
        "x_data": [1, 2, 3, 4],
        "y_data": [10, 11, 12, 13],
        "circle_data": [40, 60, 80, 100]
    }

    bb_chart = bubble.Bubble(data, title)
    bb_data = bb_chart.draw_graph(data['x_data'], data['y_data'], data['circle_data'])

    file_name = "Bubble_viz_1.html"
    bb_chart.generate_file(chart_data=bb_data, filename=file_name, open_chart=False)
    return render_template(file_name)

"""Main entry point for application"""
def main():
    app.run(debug=True, host='0.0.0.0')

main()

