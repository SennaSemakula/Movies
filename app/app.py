from flask import Flask, render_template, request
from pprint import pprint
from charts import graph
from charts import bubble, plot
from jinja2 import Environment, FileSystemLoader
from os import path
from datetime import datetime
import random

global monthly_val
monthly_val = None

"""Main application file"""
app = Flask(__name__)
template_path = "{}/templates".format(path.dirname(path.abspath(__file__)))
env = Environment(loader=FileSystemLoader(template_path))

@app.route('/')
def index():
    template = env.get_template('index.html')
    return template.render(name='SENNA')


@app.route('/results', methods=['GET', 'POST'])
def result():
    template_new = env.get_template('result.html')

    """Selecting visualisation graph"""

    if request.method == 'POST':
        result = request.form

        total = float(result['years']) * (float(result['monthly']) * 12.0)
        return render_template(template_new, result=result, total=total)
    else:
        return "FAIL!"

@app.route('/viz/plot/<title>', methods=['GET', 'POST'])
def scatter(title):
    """When routed, will display visualisation"""
    months = ['2018-0{}-01'.format(str(month)) for month in range(1, 10)]

    #Append the unique ones
    for month in range(3):
        months.append('2018-1{}-01'.format(month))

    global monthly_val

    if request.method == 'POST':
        result = request.form
        monthly_val = int(result['monthly'])

    form_title = request.form['title']

    data = {
        "x_data": months,
        "y_data": [monthly_val * 1 for i in range(0, 12)],
    }

    sc_chart = plot.Plot(data, form_title)
    sc_data = sc_chart.draw_graph(data['x_data'], data['y_data'])

    file_name = "Scatter_1.html"
    sc_chart.generate_file(chart_data=sc_data, filename=file_name, open_chart=False)

    return render_template(file_name, lol_value="http://localhost:5000/viz/plot/lol")

"""Displays a bubble chart visualiastion"""
@app.route('/viz/bubble/<title>')
def bubble(title):
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

