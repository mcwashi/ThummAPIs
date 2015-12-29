from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)

class Users(db.Model):
    __tablename__ = 'User1'
    id = db.Column('id', db.Integer, primary_key=True)
    User = db.Column('User', db.Unicode)

    def __init__(self, id, User):
        self.id = id
        self.User = User
