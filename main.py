from flask import Flask, jsonify, request
import requests
from coin_data import get_coin_data, retrieve_coin_data
from coin_dbase import select_currency, insert_currency, delete_currency, update_currency, insert_user, select_user
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()
role = ''

@app.route("/") 
def welcome():
    return('<h1>Welcome! We are group 7.</h1>')

# GET
@app.route("/<symbol>", methods=['GET'])
@auth.login_required
def get_data(symbol):
    try:
        id = select_currency(symbol)
        print(id)
        api_data = retrieve_coin_data(id)
        return jsonify(api_data), 200
    except:
        return jsonify({'error':'currency not found'}), 404


# POST
@app.route('/add', methods=['POST'])
@auth.login_required(role=['admin', 'moderator'])
def create_currency_record():
    if not request.json or not all(k in request.json for k in ['id','symbol']):
        return jsonify({'error':'error'}), 400
    new_record = {
        'id': request.json['id'],
        'symbol' : request.json.get('symbol', '')
    }
    insert_currency(new_record['id'], new_record['symbol'])
    return jsonify({'message':'new currency created.'}), 201


# PUT
@app.route('/update', methods=['PUT'])
@auth.login_required(role=['admin', 'moderator'])
def update_record():
    if not request.json or not all(k in request.json for k in ['id','symbol']):
        return jsonify({'error':'error'}), 400
    new_record = {
        'id': request.json['id'],
        'symbol' : request.json.get('symbol', ''), 
    }
    status = update_currency(new_record['id'], new_record['symbol'])
    return jsonify({'success': status}), 201


# DELETE
@app.route('/delete/<symbol>', methods=['DELETE'])
@auth.login_required(role=['admin', 'moderator'])
def delete_a_currency(symbol): 
    
    status = delete_currency(symbol)
    if status:
        return jsonify({'success': f'Deleted {symbol}'}), 200
    else:    
        return jsonify({'error': 'Record not found'}), 404     

# POST
@app.route('/add_user', methods=['POST'])
@auth.login_required(role='admin')
def create_a_user():
    if not request.json or not all(k in request.json for k in ['userID', 'pw', 'role']):
        return jsonify({'error':'the new user needs to have user name, password, and role'}), 400
    new_record = {
        'userID': request.json.get('userID', ''),
        'pw' : request.json.get('pw', ''),
        'role' : request.json.get('role', ''),
    }
    insert_user(new_record['userID'], generate_password_hash(new_record['pw']), new_record['role'])
    return jsonify({'message':'new user created'}), 201
       
        
@auth.verify_password
def authenticate(userID, pw):
    role = 0
    if userID and pw:       
        account = select_user(userID)  
        if account and check_password_hash(account[1], pw):
            role = account[2]
            return role
        else:
            return False
    return False


@auth.get_user_roles
def get_user_roles(role):       
    return role
    
    
@auth.error_handler
def unauthorized():
    return jsonify({'error': 'Unauthorized access'}), 401
      

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug='True')

