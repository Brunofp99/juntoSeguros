from sql_alchemy import banco

class UserModel(banco.Model):
    __tablename__ = 'usuarios'

    id = banco.Column(banco.Integer, primary_key=True, unique=True, nullable=False)
    login = banco.Column(banco.String(40), nullable=False, unique=True)
    senha = banco.Column(banco.String(40), nullable=False)

    def __init__(self, login, senha):
        self.login = login
        self.senha = senha
    
    def json(self):
        return {
            'id': self.id,
            'login': self.login
        }
    
    def save_user(self):
        banco.session.add(self)
        banco.session.commit()

    def update_hotel(self, login, estrelas, diaria, cidade):
        self.nome = nome
        self.estrelas = estrelas
        self.diaria = diaria
        self.cidade = cidade

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
        banco.session.delete(self)
        banco.session.commit()
