#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/<username>')
def user(username):
    return f"<h1>Welcome to my page! {username}</h1>"
