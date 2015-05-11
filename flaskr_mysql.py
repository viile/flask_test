#/usr/bin/python
# -*- coding: utf-8 -*-
import os
from flask import Flask, request, session,redirect, url_for, abort,render_template, flash
from flask import Flask
import MySQLdb
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/flask'
app.config['SECRET_KEY']='development key'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(320), unique=True)
    phone = db.Column(db.String(32), nullable=False)

    def __init__(self, username, password, phone):
        self.username = username
        self.password = password
        self.phone= phone
    def __repr__(self):
        return 'User %r' % self.username

class Entries(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    text = db.Column(db.String(320), unique=True)

    def __init__(self, title, text):
        self.title = title
        self.text = text
    def __repr__(self):
        return 'title %r' % self.title

@app.route('/')
def show_entries():
    entries = Entries.query.all()
    return render_template('show_entries.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    inset=Entries(title=request.form['title'],text=request.form['text'])
    db.session.add(inset)
    db.session.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if(username and password):
             entries = User.query.filter(User.username == username,User.password == password).first()
             if(entries):
                 session['logged_in'] = True
                 flash('You were logged in')
                 return redirect(url_for('show_entries'))
             else:
                 error = 'username or password wrong'
        else:
             error = 'username or password wrong'
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
