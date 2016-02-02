from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)

class User1(db.Model):
    __tablename__ = 'User1'
    id = db.Column('id', db.Integer, primary_key=True)
    User = db.Column('User', db.Unicode)
