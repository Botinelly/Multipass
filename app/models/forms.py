from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired

class Login(FlaskForm):
    login = StringField("Email", validators = [DataRequired()])
    password = PasswordField("Senha", validators = [DataRequired()])
    remember_me = BooleanField("remember_me")

class Cadastro(FlaskForm):
    matricula = StringField("Matricula", validators = [DataRequired()])
    nome = StringField("Nome", validators = [DataRequired()])
    endereco = StringField("Endereco", validators = [DataRequired()])
    bairro = StringField("Bairro", validators = [DataRequired()])
    cidade = StringField("Cidade", validators = [DataRequired()])
    UF = StringField("UF", validators = [DataRequired()])
    CEP = StringField("CEP", validators = [DataRequired()])
    email = StringField("E-mail", validators = [DataRequired()])
    telefone = StringField("Telefone Fixo")
    celular = StringField("Celular", validators = [DataRequired()])
    senha = PasswordField("Senha", validators = [DataRequired()])

class Temp(FlaskForm):
    nome = StringField("Nome", validators = [DataRequired()])
    email = StringField("E-mail", validators = [DataRequired()])
    matricula = StringField("Matricula", validators = [DataRequired()])

class Update(FlaskForm):
    matricula = StringField("Matricula", validators = [DataRequired()])
    nome = StringField("Nome", validators = [DataRequired()])
    endereco = StringField("Endereco", validators = [DataRequired()])
    bairro = StringField("Bairro", validators = [DataRequired()])
    cidade = StringField("Cidade", validators = [DataRequired()])
    UF = StringField("UF", validators = [DataRequired()])
    CEP = StringField("CEP", validators = [DataRequired()])
    email = StringField("E-mail", validators = [DataRequired()])
    telefone = StringField("Telefone Fixo")
    celular = StringField("Celular", validators = [DataRequired()])
