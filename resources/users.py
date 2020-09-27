from flask_restful import Resource, reqparse
from models.users import UserModel
from resources.filters import normalize_path_params, query_with_city, query_without_city
from flask_jwt_extended import create_access_token, jwt_required
import bcrypt
import sqlite3

update = reqparse.RequestParser()
update.add_argument('login', type=str)
update.add_argument('password', type=str)
update.add_argument('city', type=str)

attributes = reqparse.RequestParser()
attributes.add_argument('login', type=str, required=True, help="Teh field 'login' cannot be left blank")
attributes.add_argument('password', type=str, required=True, help="Teh field 'password' cannot be left blank")
attributes.add_argument('city', type=str)

path_params = reqparse.RequestParser()
path_params.add_argument('city', type=str)
path_params.add_argument('limit', type=float)
path_params.add_argument('offset', type=float)

class Users(Resource):
    def get(self):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        data = path_params.parse_args()
        valid_data = { key:data[key] for key in data if data[key] is not None }
        params = normalize_path_params(**valid_data)

        if params.get('city'):
            tupla = tuple([params[key] for key in params])
            result = cursor.execute(query_with_city, tupla)
        else:
            tupla = tuple([params[key] for key in params])
            result = cursor.execute(query_without_city, tupla)
        
        users = []

        for column in result:
            users.append({
                'id': column[0],
                'login': column[1],
                'city': column[3]
            })

        return { 'users': users }

class User(Resource):
    @jwt_required
    def get(self, id):
        user = UserModel.find_user(id)
        if user:
            return user.json()
        return { 'message': 'user not found' }, 404

    @jwt_required
    def delete(self, id):
        user_find = UserModel.find_user(id)
        if user_find:
            try:
                user_find.delete_user()
            except:
                return { 'message': 'An internal error ocurred trying to delete user' }, 500
            return { 'message': 'user deleted' }
        return { 'message': "The user '{}' does not exist".format(id) }, 404

class UserRegister(Resource):
    def post(self):
        data = attributes.parse_args()

        city = data['city'].lower().capitalize()
        data['city'] = city

        if UserModel.find_by_login(data['login']):
            return { 'massage': "The login {} alredy exists.".format(data['login']) }
        
        password_encrypt = self.encrypt_password(data['password'])
        data['password'] = password_encrypt

        user = UserModel(**data)
        user.save_user()

        return { "message": "User cread successfully" }, 201
    
    @classmethod
    def encrypt_password(cls, password):
        hash_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        return hash_password

class UserUpdate(Resource):
    @jwt_required
    def put(self, id):
        data = update.parse_args()

        user_find = UserModel.find_user(id)

        if user_find:
            if data['login']:
                user_find.update_user_login(data['login'])

            if data['password']:
                password_encrypt = self.encrypt_password(data['password'])
                data['password'] = password_encrypt
                user_find.update_user_password(data['password'])

            if data['city']:
                user_find.update_user_city(data['city'])

            user_find.save_user()
            return user_find.json()
        return {'message': 'this user id {} dont have a register'.format(id)}
    
    @classmethod
    def encrypt_password(cls, password):
        hash_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        return hash_password

class UserLogin(Resource):
    @classmethod 
    def post(cls):
        data = attributes.parse_args()

        user = UserModel.find_by_login(data['login'])

        if user and cls.valid_password(data['password'], user.password):
            token_de_acesso = create_access_token(identity=user.id)
            return { 'access_token': token_de_acesso }, 200
        return { 'message': 'The user name or password is incorrect' }, 401
    
    @classmethod
    def valid_password(cls, password_typed, hash_password):
        return bcrypt.hashpw(password_typed.encode('utf-8'), hash_password) == hash_password

