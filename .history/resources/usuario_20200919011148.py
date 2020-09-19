from flask_restful import Resource, reqparse
from models.usuario import UserModel
from flask_jwt_extended import create_access_token, jwt_required, get_raw_jwt
from werkzeug.security import safe_str_cmp
from blacklist import BLACKLIST
import bcrypt

atributos = reqparse.RequestParser()
atributos.add_argument('login', type=str, required=True, help="Teh field 'login' cannot be left blank")
atributos.add_argument('senha', type=str, required=True, help="Teh field 'senha' cannot be left blank")

class Users(Resource):
    def get(self):
        return { 'usuarios': [user.json() for user in UserModel.query.all()] }

class User(Resource):
    @jwt_required
    def get(self, id):
        user = UserModel.find_user(id)
        if user:
            return user.json()
        return { 'message': 'user not found' }, 404

    @jwt_required
    def delete(self, id):
        user_encontrado = UserModel.find_user(id)
        if user_encontrado:
            try:
                user_encontrado.delete_user()
            except:
                return { 'message': 'An internal error ocurred trying to delete user' }, 500
            return { 'message': 'user deleted' }
        return { 'message': "The user '{}' does not exist".format(id) }, 404

class UserRegister(Resource):

    def post(self):

        dados = atributos.parse_args()

        if UserModel.find_by_login(dados['login']):
            return { 'massage', "The login {} alredy exists.".format(dados['login']) }
        
        senha_incriptada = self.incripta_senha(dados['senha'])
        dados['senha'] = senha_incriptada

        user = UserModel(**dados)
        user.save_user()

        return { "message": "User cread successfully" }, 201
    
    @classmethod
    def incripta_senha(cls, senha):
        hash_senha = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())
        return hash_senha

class UserUpda

class UserLogin(Resource):
    @classmethod 
    def post(cls):
        dados = atributos.parse_args()

        user = UserModel.find_by_login(dados['login'])

        if user and cls.valida_senha(dados['senha'], user.senha):
            token_de_acesso = create_access_token(identity=user.id)
            return { 'access_token': token_de_acesso }, 200
        return { 'message': 'the user name or password is incorrect' }, 401
    
    @classmethod
    def valida_senha(cls, senha_digitada, hash_senha):
        return bcrypt.hashpw(senha_digitada.encode('utf-8'), hash_senha) == hash_senha

class UserLogout(Resource):
    @jwt_required
    def post(self):
        jwt_id = get_raw_jwt()['jti']
        BLACKLIST.add(jwt_id)
        return { 'message': 'Logged out successfully' }, 200
