from sql_alchemy import database

class UserModel(database.Model):
    __tablename__ = 'users'

    id = database.Column(database.Integer, primary_key=True, unique=True, nullable=False)
    login = database.Column(database.String(40), nullable=False, unique=True)
    password = database.Column(database.String(40), nullable=False)
    city = database.Column(database.String(50))

    def __init__(self, login, password, city):
        self.login = login
        self.password = password
        self.city = city
    
    def json(self):
        return {
            'id': self.id,
            'login': self.login,
            'city': self.city
        }
    
    def save_user(self):
        database.session.add(self)
        database.session.commit()

    def update_user_login(self, login):
        self.login = login

    def update_user_password(self, password):
        self.password = password
        
    def update_user_city(self, city):
        self.city = city

    @classmethod
    def find_user(cls, id):
        user = cls.query.filter_by(id=id).first()
        if user:
            return user
        return None

    @classmethod
    def find_by_login(cls, login):
        user = cls.query.filter_by(login=login).first()
        if user:
            return user
        return None

    def delete_user(self):
        database.session.delete(self)
        database.session.commit()
