import flask
import requests
from bs4 import BeautifulSoup as bs
import FileCreate
import TableExchange
from flask import request, json
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
    if request.is_json == True:
        content = request.get_json()
        uid = content["uid"]
        password = content["password"]
        year = content["year"]
        sem = content["sem"]
    else:
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
    os.remove('./table')
    os.remove(uid+'.json')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
