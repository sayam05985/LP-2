
from flask import Flask
app = Flask(name)

@app.route('/')
def home():
    return 'Hello from Google App Engine!'
