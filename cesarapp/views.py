from flask import Flask, render_template, request, url_for, flash, redirect
import json
from flask_sqlalchemy import SQLAlchemy
from . import app

def decrypt(crypt):
    decrypt = ""
    for i in crypt:
        letter = ord(i) - 96
        decrypt = decrypt + chr(((letter - 13) % 26) + 96)
    return decrypt

def crypt(decrypt):
    crypt = ""
    for i in decrypt:
        letter = ord(i) - 96
        crypt = crypt + chr(((letter + 13) % 26) + 96)
    return crypt

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        message_decrypt = request.form['textcrypt']
        message_crypt = request.form['textdecrypt']
    else:
        message_decrypt = ""
        message_crypt = ""
    return render_template("index.html", message_decrypt=decrypt(message_decrypt), message_crypt=crypt(message_crypt))

@app.route('/login')
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run()
