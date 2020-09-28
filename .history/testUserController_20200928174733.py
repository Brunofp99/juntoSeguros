from unittest import TestCase, main
from resources.users import Users, User, UserRegister, UserUpdate, UserLogin
from createApp import create_app

app = create_app()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.app_context().push()

class TesteUserModel(TestCase):
    data = {
        "login": "luafalce10@hotmail.com",
        "password": "12345",
        "city": "Curitiba"
    }

    new_login = "testeLogin1@hotmail.com"
    new_password = "teste"
    new_city = "São paulo"

    users = Users()
    user = User()
    user_register = UserRegister()
    user_update = UserUpdate()
    user_login = UserLogin()

    @app.route('/users')
    def test_list_users(self):
        print('test')
        assert self.users.get()
    
  
# if __name__ == '__main__':
with app.test_client() as client:
    client.get('/users')