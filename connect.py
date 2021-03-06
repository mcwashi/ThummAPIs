from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.ext.restless import APIManager

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)

class User1(db.Model):
    #__tablename__ = 'User1'
    id = db.Column('id', db.Integer, primary_key=True)
    User = db.Column('User', db.Unicode)

manager = APIManager(app, flask_sqlalchemy_db = db)
manager.create_api(User1)

if __name__ == "__main__":
    app.run(debug=True)
