import flask
import requests
from bs4 import BeautifulSoup as bs
import FileCreate
import TableExchange
from flask import request, json
import os
import time

app = flask.Flask(__name__)



@app.route('/', methods=['GET'])
def home():
    return "<h1>Hello Flask!</h1>"

@app.route('/geTable', methods=['POST'])
def result():
     if request.method == 'POST':
         uid = request.values['uid']
         password = request.values['password']
         year = request.values['year']
         sem = request.values['sem']
         FileCreate.geTable(uid,password,year,sem)
         TableExchange.Exchange(uid)
         uid = uid+".json"
         json_url = os.path.join(app.root_path, uid)
         data = json.load(open(json_url))
         return data    

# @app.route('/oldTable', methods=['GET'])
# def old():
#     json_url = os.path.join(app.root_path, )
#     data = json.load(open(json_url))
#     return data

    
if __name__ == '__main__':
    app.run(port=8080)
