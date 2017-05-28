# -*- coding: utf-8 -*-
# Flask app that handle application logic


import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import FileDialog
import base64
import json

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
files = None


@app.before_request
def before_request():
    pass


@app.teardown_request
def teardown_request(exception):
    pass


# @app.route('/open_folder/', methods=['GET'])
# def add_folder():
#     root = tk.Tk()
#     root.withdraw()
#     root.overrideredirect(True)
#     root.geometry('0x0+0+0')
#     root.deiconify()
#     root.lift()
#     root.focus_force()
#     file_path = tkFileDialog.askdirectory()
#     root.destroy()
#
#     print("FILEPATH: " + file_path)
#
#     return file_path


@app.route('/', methods=['GET'])
def index():
    random_json = ["Data One", "Data Two", "Data Three", "Data Four"]
    random_json = json.dumps(random_json)
    random_json = base64.b64encode(random_json.encode())
    return render_template('index.html', random_json=random_json)


@app.route('/about/', methods=['GET'])
def about():
    return render_template('about.html')


@app.route('/save_data/', methods=['POST'])
def save_data():
    random_json = request.form["random_json"]
    random_json = base64.b64decode(random_json)
    random_json = json.loads(random_json)

    for data in random_json:
        print(data)

    return "Success"


if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True, use_reloader=True)
