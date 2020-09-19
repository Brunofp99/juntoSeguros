from flask import Flask, jsonify
from flask_restful import Api
from resources.usuario import User, Users, UserRegister, UserLogin, UserLogout, User
from flask_jwt_extended import JWTManager
from blacklist import BLACKLIST

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'DontTellAnyone'
app.config['JWT_BLACKLIST_ENABLED'] = True
api = Api(app)
jwt = JWTManager(app)

@app.before_first_request
def create_bd():
    banco.create_all()

@jwt.token_in_blacklist_loader
def verifica_blacklist(token):
    return token['jti'] in BLACKLIST

@jwt.revoked_token_loader
def token_de_acesso_invalidado():
    return jsonify({'message': 'You have been logged out.'}), 401

api.add_resource(Users, '/usuarios')
api.add_resource(UserLogin, '/usuario/token')
api.add_resource(UserLogout, '/usuario/delete_token')
api.add_resource(UserRegister, '/usuario/cadastro')
api.add_resource(User, '/usuarios/<int:id>')
api.add_resource(UserUpdate, '/usuarios/<int:id>')

if __name__ == '__main__':
    from sql_alchemy import banco
    banco.init_app(app)
    app.run(debug=True)
