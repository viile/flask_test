#/usr/bin/python
# -*- coding: utf-8 -*-
import os
from flask import Flask, g,current_app,session,request, session,redirect, url_for, abort,render_template, flash,make_response
import MySQLdb
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required

class NameForm(Form):
	name = StringField('What is your name?',validators=[Required()])
	submit = SubmitField('Submit')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'wtf come'
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
@app.route('/name/',methods=['GET','POST'])
def name():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        flash('i will like you ')
        form.name.data = ''
        return redirect(url_for('name'))
    return render_template('name.html',form=form,name=session.get('name'))
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'),404
app.debug = True
app.run(host='0.0.0.0')
