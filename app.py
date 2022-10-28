from flask import Flask
import json
from flask import jsonify
from flask import request
from flask_cors import CORS
from waitress import serve


app=Flask(__name__)

#primera ruta
@app.route('/')
def index():
    return "hola mundo"
    
@app.route('/usuaruio/<post:post_id>')
def show_post(post_id):
    return f'post {post_id}'
    

    