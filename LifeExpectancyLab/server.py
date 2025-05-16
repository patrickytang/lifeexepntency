# flask --app data_server run
from flask import Flask
from flask import request
from flask import render_template
import json


app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def index():
    
    f = open("data/life_expectancy.json", "r")
    dater = json.load(f)
    f.close()
    return render_template('index.html', data=dater)


@app.route('/year')
def year():
    requested_year = request.args.get('year')
    return render_template('year.html', curYear = requested_year, )

@app.route("/line_graph")
def linegr():
    f = open("data/life_expectancy.json", "r")
    dater = json.load(f)
    f.close()
    print(dater)
    #return render_template("line_graph.svg",data=dater)

app.run(debug=True)
