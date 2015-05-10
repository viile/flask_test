#/usr/bin/python
# -*- coding: utf-8 -*-
import os
from flask import Flask, g,current_app,session,request, session,redirect, url_for, abort,render_template, flash,make_response
import MySQLdb
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
@app.route('/')
def index():
    return 'hello'

@app.route('/<name>')
def hello(name):
    if(name == 'viile'):
        return 'Bad Request',404
    return render_template('user.html',name=name)

@app.route('/cookie')
def cookie():
    response = make_response('carries a cookie')
    response.set_cookie('answer','42')
    return response
app.debug = True
app.run(host='0.0.0.0')
