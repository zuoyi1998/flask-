from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from datetime import datetime
import pymysql

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:zy980215@127.0.0.1:3306/board'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY']='yzuo'

db=SQLAlchemy(app)

class Admin(db.Model):
    __tablename__='admin'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(32),nullable=False,unique=True)
    password=db.Column(db.String(64),nullable=False)
    tags=db.relationship('Tag',backref='admin')

class User(db.Model):
    __tablename__='user'
    id=db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(32), nullable=False,unique=True)
    password = db.Column(db.String(64), nullable=False)
    messages=db.relationship('Message',backref='user')

class Message(db.Model):
    __table__name='message'
    id=db.Column(db.Integer,primary_key=True)
    content=db.Column(db.String(256),nullable=False)
    create_time=db.Column(db.DateTime,default=datetime.now)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    tags=db.relationship('Tag',secondary='message_to_tag',backref='messages')

class Tag(db.Model):
    __tablename__='tag'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(10),nullable=False,unique=True)
    admin_id=db.Column(db.Integer,db.ForeignKey('admin.id'))

class MessageToTag(db.Model):
    __tablename__='message_to_tag'
    id=db.Column(db.Integer,primary_key=True)
    message_id=db.Column(db.Integer,db.ForeignKey('message.id',ondelete='CASCADE'))
    tag_id=db.Column(db.Integer,db.ForeignKey('tag.id',ondelete='CASCADE'))



if __name__=='__main__':
    db.create_all()
    #db.drop_all()