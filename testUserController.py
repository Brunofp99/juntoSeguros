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

  
if __name__ == '__main__':
    main()