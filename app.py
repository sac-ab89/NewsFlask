from flask import Flask, jsonify
import peewee as pw
import logging,logging.handlers
import time
import sys
from flask import g
from flask import request


app = Flask(__name__)
app.config.from_object('settings.config')

db = pw.MySQLDatabase(app.config['DB_NAME'], host=app.config['DB_HOST'], port=app.config['DB_PORT'],
                      user=app.config['DB_USER'], passwd=app.config['DB_PASS'])

from controllers.news import news

app.register_blueprint(news)

@app.before_request
def _db_connect():
    db.connect()