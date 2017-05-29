from app import db

class User(db.Model):
    __tablename__ = "UEA_ALUNO"

    alu_matricula = db.Column(db.String(20), primary_key = True)
    alu_nome = db.Column(db.String(50))
    alu_endereco = db.Column(db.String(100))
    alu_bairro = db.Column(db.String(50))
    alu_cidade = db.Column(db.String(50))
    alu_UF = db.Column(db.String(2))
    alu_CEP = db.Column(db.String(8))
    alu_email = db.Column(db.String(50), unique = True)
    alu_telefone = db.Column(db.String(15))
    alu_celular = db.Column(db.String(15))
    alu_senha = db.Column(db.String(30))


    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return false

    def get_id(self):
        return str(self.alu_matricula)

    def __init__(self, alu_matricula, alu_nome, alu_endereco, alu_bairro,alu_cidade, alu_UF, alu_CEP, alu_email, alu_telefone, alu_celular, alu_senha): #, alu_foto
        self.alu_matricula = alu_matricula
        self.alu_nome = alu_nome
        self.alu_endereco = alu_endereco
        self.alu_bairro = alu_bairro
        self.alu_cidade = alu_cidade
        self.alu_UF = alu_UF
        self.alu_CEP = alu_CEP
        self.alu_email = alu_email
        self.alu_telefone = alu_telefone
        self.alu_celular = alu_celular
        self.alu_senha = alu_senha

    def __repr__(self):
        return "%s" % self.alu_nome
