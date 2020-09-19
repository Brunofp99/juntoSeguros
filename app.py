from flask import Flask, jsonify
from flask_restful import Api
from resources.users import User, Users, UserRegister, UserLogin, UserUpdate
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'oB61d75vwh8Rq76CYsiZ4l0bHVcDUThnhax6cNzYt4Qif4JQrVpc9kMlYlp46ryhUUp6m7IeCB_0V8v7igmLHCwdokgue_AoGMqTJBl0YrIQdm3QKtzbVyfbmdLoRfPIudtXiEDSrOoNxFKe24BLTGHuj6b98Yzytfmb1-xyvFojLJCXWH2n_LscfNKXShloR6HbFdq6MFLmgitIV5LQ6XuII2Fyyect_7ABlGyKHizWcSy10O7UaR1gF7XdVvR6cqYPLs3h7r1Jq2vn92sY776_czJf_uFn5Fc836xidgDXa7Ctc47DTAwyDG52lkjKPcqrlzaz3g2muQvmyRtrWw'
api = Api(app)
jwt = JWTManager(app)

@app.before_first_request
def create_bd():
    database.create_all()

api.add_resource(Users, '/users')
api.add_resource(UserLogin, '/users/token')
api.add_resource(UserRegister, '/users/register')
api.add_resource(User, '/users/<int:id>')
api.add_resource(UserUpdate, '/users/alter/<int:id>')

if __name__ == '__main__':
    from sql_alchemy import database
    database.init_app(app)
    app.run(debug=True)
