import flask
import requests
from bs4 import BeautifulSoup as bs
import FileCreate
import TableExchange
from flask import request, json, jsonify
import os
import time
from flask_cors import CORS
from flask_cors import cross_origin

app = flask.Flask(__name__)
CORS(app, cors_allowed_origins='*')


@app.route('/', methods=['GET'])
def home():
    return "<h1>Hello Flask!</h1>"

@app.route('/geTable', methods=['POST'])
@cross_origin()
def result():
    if request.is_json == True :
        content = request.get_json()
        uid = content["uid"]
        password = content["password"]
        year = content["year"]
        sem = content["sem"]
        target = content["target"]

    else:
        uid = request.values['uid']
        password = request.values['password']
        year = request.values['year']
        sem = request.values['sem']
        target = request.values['target']
        
    if target == "":
        target = uid

    FileCreate.geTable(uid,password,year,sem,target)
    TableExchange.Exchange(target)
    target = target+".json"
    json_url = os.path.join(app.root_path, target)
    data = json.load(open(json_url))
    return data 
    os.remove("./table")
    os.remove(target+".json")

# @app.route('/oldTable', methods=['GET'])
# def old():
#     json_url = os.path.join(app.root_path, )
#     data = json.load(open(json_url))
#     return data

    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
