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
import base64
import json
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5 as PKCS1_signature
from Crypto.Cipher import PKCS1_v1_5 as PKCS1_cipher


app = flask.Flask(__name__)
CORS(app, cors_allowed_origins='*')

def key_gen():
    # generate key
    random_generator = Random.new().read
    key = RSA.generate(2048, random_generator)
    # get public key
    public_key = key.publickey()
    # get public key in string
    public_key_string = public_key.exportKey()
    # get private key in string
    private_key_string = key.exportKey()

    # get keys location
    with open("./keys/config.json","r") as f:
        config = json.load(f)
    private_key_location = config["private_key_location"]

    with open("./keys/config.json","r") as f:
        config = json.load(f)
    public_key_location = config["public_key_location"]

    # write keys to file
    with open(public_key_location, "wb") as f:
        f.write(public_key_string)

    with open(private_key_location, "wb") as f:
        f.write(private_key_string)

def get_key(key_file):
    with open(key_file) as f:
        data = f.read()
        key = RSA.importKey(data)

    return key

def decrypt(password):
    # get config file
    with open("./keys/config.json","r") as f:
        config = json.load(f)
    private_key_location = config["private_key_location"]
    # get private key
    private_key = get_key(private_key_location)
    # decrypt password
    decrypted_password = PKCS1_cipher.new(private_key).decrypt(base64.b64decode(password),0).decode('utf-8')
    return decrypted_password



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