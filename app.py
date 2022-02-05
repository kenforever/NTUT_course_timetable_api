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
from encrypt import *
from get_semester_info import *

app = flask.Flask(__name__)
CORS(app, cors_allowed_origins='*',support_credentials=True)

@app.route('/', methods=['GET'])
def home():
    return "<h1>{flag:this_is_not_a_flag}}</h1>"

@app.route('/pubkey', methods=['GET'])
def pub_key():
        # get config file
    with open("./keys/config.json","r") as f:
        config = json.load(f)
    public_key_location = config["public_key_location"]
    # get public key
    with open(public_key_location) as f:
        pubkey = f.read()
        
    pubkey = {"pubkey":pubkey}

    return pubkey


@app.route('/sec_get_semesters_info', methods=['POST'])
@cross_origin()
def sec_semesters_info():

    if request.is_json == True :
        content = request.get_json()
        uid = content["uid"]
        password = decrypt(content["password"])
        try:
            target = content["target"]
        except KeyError:
            target = uid

    semesters = get_semester_info(uid,password,target)
    # return data
    return jsonify(semesters)


@app.route('/geTable', methods=['POST'])
@cross_origin()
def getable():
    if request.is_json == True :
        content = request.get_json()
        uid = content["uid"]
        password = content["password"]
        year = content["year"]
        sem = content["sem"]
        try:
            target = content["target"]
        except KeyError:
            target = uid

    FileCreate.geTable(uid,password,year,sem,target)
    TableExchange.Exchange(target,year,sem)
    target_json = "./temps/"+target+".json"
    json_url = os.path.join(app.root_path, target_json)
    data = json.load(open(json_url))
    os.remove("./temps/"+target)
    os.remove("./temps/"+target+"_code")
    os.remove(target_json)
    return data

@app.route('/sec_geTable', methods=['POST'])
@cross_origin()
def sec_getable():
    if request.is_json == True :
        content = request.get_json()
        uid = content["uid"]
        password = decrypt(content["password"])
        year = content["year"]
        sem = content["sem"]
        try:
            target = content["target"]
        except KeyError:
            target = ""

    if target == "":
        target = uid
    FileCreate.geTable(uid,password,year,sem,target)
    TableExchange.Exchange(target,year,sem)
    target_json = "./temps/"+target+".json"
    json_url = os.path.join(app.root_path, target_json)
    data = json.load(open(json_url))
    os.remove("./temps/"+target)
    os.remove("./temps/"+target+"_code")
    os.remove(target_json)
    return data
    
if __name__ == '__main__':

    app.debug=True
    app.run(host="0.0.0.0", port=8080)



try:
        # keys check
    with open("./keys/config.json","r") as f:
        config = json.load(f)
    private_key_location = config["private_key_location"]
    with open(private_key_location) as f:
        pass
except FileNotFoundError:
    key_gen()

try:
    os.makedirs("./temps")
except FileExistsError:
    pass