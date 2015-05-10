#!/usr/bin/python

from flask import Flask
import MySQLdb
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/flask'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(320), unique=True)
    phone = db.Column(db.String(32), nullable=False)
  
    def __init__(self, username, email, phone):
        self.username = username
        self.email = email
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

if __name__ == '__main__':
    db.create_all()
    '''
    #insert example
    inset=User(username='user',email='user@example.com',phone='18672781552')
    db.session.add(inset)
    db.session.commit()
    #select example
    select = User.query.filter_by(username='admin').first()
    print 1
    print select.id
    print 2
    print User.query.filter(User.email.endswith('@example.com')).all
    print 3
    print User.query.filter(User.phone != '123456').first()
    print 4
    print User.query.filter(not (User.phone == '18672781552')).first()
    #print User.query.filter(or_(User.phone != '123456',User.username.endswith('@'))).first()
    #print User.query.filter(and_(User.phone != '123456',User.username.endswith('@'))).first()
    data_all = User.query.limit(10).all()
    for i in range(len(data_all)):
        print i
        print data_all[i].username+" "+data_all[i].email+" "+data_all[i].phone
    #update example
    news=User.query.all()
    print news
    news[1].username='test'
    db.session.commit() 
    #delete example
    name=User.query.filter_by(username = 'test').first()
    db.session.delete(name)
    db.session.commit()
    '''
