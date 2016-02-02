from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.ext.restless import APIManager

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)

class EventLikes(db.Model):
    __tablename__ = 'event_likes'
    id = db.Column('id', db.Integer, primary_key=True)
    eventId = db.Column('event_id', db.Integer)
    userId = db.Column('user_id', db.Integer)
    type = db.Column('type', db.Integer)
    dateAdded = db.Column('date_added', db.DateTime)

class User1(db.Model):
    __tablename__ = 'User1'
    id = db.Column('id', db.Integer, primary_key=True)
    User = db.Column('User', db.Unicode)

manager = APIManager(app, flask_sqlalchemy_db = db)
manager.create_api(EventLikes)
manager.create_api(User1)
#manager.create_api(User, primary_key='username')


@app.route('/api/login/<int:id>', methods=['GET'])
def get_User(id):
    user = [user for user in User1 if user['id'] == id]
    if len(task) == 0:
        abort(404)
    return jsonify({'user': user[0]})


if __name__ == "__main__":
    app.run(debug=True)
