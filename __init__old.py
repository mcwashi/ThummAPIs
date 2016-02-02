#!flask/bin/python
from flask import Flask, jsonify, request
from flask import abort
from Thumm import *


app = Flask(__name__)

data = [
    {
        'id': 2,
        'name': u'Buy groceries',
        'username': '',
        'userEmail': 'john@doe.com',
        'userPassword': 'testpassword',
        'facebook_id': '',
        'location': 'Los Angelos, United States',
        'image': 'shower_in_thunderstorm_300.jpg',
        'key': '',
        'status': '1',
        'genre': 'm',
        'date_added':'2014-02-12 00:00:00',
        'mode': '0',
        'last_login':'2014-02-13 13:58:16',
        'mobile': '+4023432423423',
        'token': '4cds7cr6o@1392299947ym'

    },
    {
        'id': 4,
        'name': u'Buy groceries',
        'username': '',
        'userEmail': 'mike@doe.com',
        'userPassword': 'testpassword',
        'facebook_id': '',
        'location': 'Los Angelos, United States',
        'image': 'shower_in_thunderstorm_300.jpg',
        'key': '',
        'status': '1',
        'genre': 'm',
        'date_added':'2014-02-12 00:00:00',
        'mode': '0',
        'last_login':'2014-02-13 13:58:16',
        'mobile': '+4023432423423',
        'token': '4cds7cr6o@1392299947ym'
    }
]

result = [
    {
        'code': '0',
        'description': 'Everything ok!'
    }
]


catergories = [
    {
        'id': '1',
        'category': 'Religious',
        'map_image': 'religious_map.png',
        'image': 'religious.png',
        'duration': '3'
    },
    {
        'id': '2',
        'category': 'Professional',
        'map_image': 'professional_map.png',
        'image': 'professional.png',
        'duration': '3'
    },
    {
        'id': '3',
        'category': 'Bar',
        'map_image': 'bar_map.png',
        'image': 'bar.png',
        'duration': '3'
    }

]



#@app.route('/api/login/<int:user_id>', methods=['GET'])
#@app.route('/todo/api/v1.0/task', methods=['GET'])
#def get_user(user_id):
#    user = [user for user in data if user['id'] == user_id]
#    if len(user) == 0:
#        abort(404)
#    return jsonify({'user': user[0]})


@app.route('/api/login', methods=['GET'])
def get_login():
    userEmail = request.args.get('email')
    #userPassword = request.args.get('password')
    #user = [user for user in data if user['email'] == userEmail and user['password'] == userPassword]
    user = [user for user in data if user['userEmail'] == userEmail]
    if len(user) == 0:
        abort(404)
    return jsonify({'user': user[0]})

@app.route('/api/user', methods=['GET'])
def get_user():
    userId = request.args.get('id')
    idNum = int(userId)
    userToken = request.args.get('token')
    user = [user for user in data if user['id'] == idNum and user['token'] == userToken]
    #user = [user for user in data if user['id'] == idNum]
    if len(user) == 0:
        abort(404)
    return jsonify({'user': user[0]})

@app.route('/api/all_users', methods = ['GET'])
def get_users():
    return jsonify({'data': data})

@app.route('/api/categories', methods = ['GET'])
def get_catergories():
    return jsonify({'catergories': catergories})



if __name__ == '__main__':
    app.run(debug=True)
