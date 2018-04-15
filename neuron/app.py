# Flask app that handles application logic


import base64
import json

from flask import Flask
from flask import render_template
from flask import request
from neuron import get_root_path

app = Flask(__name__, static_folder=get_root_path('static'), template_folder=get_root_path('templates'))

DATA = ["Data One", "Data Two"]

@app.before_request
def before_request():
    pass


@app.teardown_request
def teardown_request(exception):
    pass


@app.route('/', methods=['GET'])
def index():
    json_data = json.dumps(DATA)
    return render_template('index.html', json_data=json_data)


@app.route('/get_data', methods=['GET'])
def get_data():
    json_data = json.dumps(DATA)
    return json_data


@app.route('/add_data/', methods=['POST'])
def add_data():
    new_value = request.form["new_value"]
    new_value = base64.b64decode(new_value)
    new_value = new_value.decode('utf-8')
    DATA.append(new_value)
    print("Added new value: '{}'".format(new_value))

    return "Success"


if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True, use_reloader=True)
