from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import pymysql

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:zy980215@127.0.0.1:3306/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY']='yzuo'

db=SQLAlchemy(app)

class Student(db.Model):
    __tablename__='student'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(64),nullable=False)
    gender=db.Column(db.Enum('男','女'),nullable=False)
    phone=db.Column(db.String(11))
    grades=db.relationship('Grade',backref='student')
    courses=db.relationship('Course',secondary='student_to_course',backref='students')

class StudentToCourse(db.Model):
    __tablename__='student_to_course'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))

class Course(db.Model):
    __tablename__='course'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(64),nullable=False)
    teacher_id=db.Column(db.Integer,db.ForeignKey('teacher.id'))
    grades=db.relationship('Grade',backref='course')

class Teacher(db.Model):
    __tablename__='teacher'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(64),nullable=False)
    gender=db.Column(db.Enum('男','女'),nullable=False)
    phone=db.Column(db.String(11))
    course=db.relationship('Course',backref='teacher')

class Grade(db.Model):
    __tablename__='grade'
    id=db.Column(db.Integer,primary_key=True)
    grade=db.Column(db.Integer,nullable=False)
    student_id=db.Column(db.Integer,db.ForeignKey('student.id'))
    course_id=db.Column(db.Integer,db.ForeignKey('course.id'))

if __name__=='__main__':
    db.create_all()
    #db.drop_all()

