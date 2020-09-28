from unittest import TestCase, main
from models.users import UserModel
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

    user_model = UserModel(**data)

    def test_save_user(self):
        self.user_model.save_user()
    
    def test_json(self):
        assert self.user_model.json()
    
    def test_update_user_login(self):
        self.user_model.update_user_login( self.new_login )

    def test_update_user_password(self):
        self.user_model.update_user_password( self.new_password )

    def test_update_user_city(self):
        self.user_model.update_user_city( self.new_city )

    def test_find_user(self):
        assert self.user_model.find_user(1)

if __name__ == '__main__':
    main()