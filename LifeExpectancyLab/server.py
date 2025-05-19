# flask --app data_server run
from flask import Flask
from flask import request
from flask import render_template
import json


app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def index():
    requested_year = request.args.get('year')
    print(requested_year, "ASDASD")
    f = open("data/life_expectancy.json", "r")
    dater = json.load(f)
    f.close()
    print("HI")
    return render_template('index.html', data=dater)


@app.route('/year')
def year():
    print("kzjlsdergkhj")
    f = open("data/life_expectancy.json", "r")
    dater = json.load(f)
    f.close()
    return render_template('year.html',year = request.args["year"],data=dater)


app.run(debug=True)
