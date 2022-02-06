from flask import Flask, jsonify,abort, request

app = Flask(__name__)

usersList = {}

@app.route('/user', methods=['GET'])
def get_users():
    return jsonify(usersList)

@app.route('/user/<id>', methods=['GET'])
def get_user(id):
    id=int(id)
    if(id in usersList):
        return jsonify({'id':id,'name':usersList[id]})
    else:
        return 'Not found',404

@app.route('/user', methods=['POST'])
def add_user():
    content = request.get_json()
    print(content)
    if(content.get('id') is not None) and (content.get('name') is not None):
        usersList[content['id']]=content['name']
        return 'User Added',201
    else:
        return 'Missing required param in message',400


@app.route('/user', methods=['PUT'])
def update_user():
    if request.is_json:
        content = request.json
        if(int(content['id']) in usersList):
            usersList[int(content['id'])]=content['name']
            return 'User Updated'
        else:
            return 'Not found',404
        return usersList[int(content['id'])]
    else:
        return 'Missing required param in message',400

@app.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
    id=int(id)
    if(id in usersList):
        usersList.pop(id)
        return 'User Deleted',204
    else:
        return 'Not found',404

if __name__ == '__main__':
    app.run(debug=True)