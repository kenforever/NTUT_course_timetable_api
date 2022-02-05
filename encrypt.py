import base64
import json
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5 as PKCS1_signature
from Crypto.Cipher import PKCS1_v1_5 as PKCS1_cipher

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
    with open(key_file,"r") as f:
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