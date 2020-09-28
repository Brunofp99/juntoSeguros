from flask import Flask, json
from sql_alchemy import database

def create_app():
    app = Flask(__name__)
    database.init_app(app)
    return app

def 