from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:sucram#4963@localhost/Thumm'
db = SQLAlchemy(app)

class Users(db.Model):
    __tablename__ = 'User1'
    id = db.Column('id', db.Integer, primary_key=True)
    User = db.Column('User', db.Unicode)
