from app import app, db,lm
from flask import render_template, flash, redirect, url_for
from app.models.forms import Login, Cadastro, Temp
from app.models.tables import User
from flask_login import login_user, logout_user, login_required

db.create_all()

@lm.user_loader
def load_user(alu_matricula):
    return User.query.filter_by(alu_matricula=alu_matricula).first()

@app.route("/index", methods=["GET", "POST"])
@app.route("/", methods=["GET", "POST"]) #methods=['GET']
def index():
    form1 = Login()
    if form1.login.data != "" and form1.password.data != ""  and form1.validate_on_submit():
        u = User.query.filter_by(alu_email=form1.login.data).first()
        p = User.query.filter_by(alu_senha=form1.password.data).first()
        if u and p:
            login_user(u)
            return redirect(url_for("home"))

    #form = Cadastro()
    #if form.matricula.data != "" and form.nome.data != "" and form.endereco.data != "" and form.bairro.data != "" and form.cidade.data != "" and form.UF.data != "" and form.CEP.data != "" and form.email.data != "" and form.telefone.data != "" and form.celular.data != "" and form.senha.data and form.validate_on_submit():
    #    temp = User(form.matricula.data, form.nome.data, form.endereco.data, form.bairro.data, form.cidade.data, form.UF.data,form.CEP.data, form.email.data, form.telefone.data, form.celular.data, form.senha.data)
    #    db.session.add(temp)
    #    db.session.commit()
    form = Temp()
    if form.nome.data != "" and form.matricula.data != "" and form.email.data != "" and form.validate_on_submit():
        return redirect(url_for("cadastro"), form = form)

    return render_template('index.html', form1 = form1, form = form)


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    form2 = Cadastro()
    if form2.matricula.data != "" and form2.nome.data != "" and form2.endereco.data != "" and form2.bairro.data != "" and form2.cidade.data != "" and form2.UF.data != "" and form2.CEP.data != "" and form2.email.data != "" and form2.telefone.data != "" and form2.celular.data != "" and form2.senha.data and form2.validate_on_submit():
        temp = User(form2.matricula.data, form2.nome.data, form2.endereco.data, form2.bairro.data, form2.cidade.data, form2.UF.data, form2.CEP.data, form2.email.data, form2.telefone.data, form2.celular.data, form2.senha.data)
        db.session.add(temp)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template('cadastro.html', form2 = form2)

@app.route("/home")
@login_required
def home():
    return render_template('home.html')

@app.route("/profile")
@login_required
def profile():
    form2 = Cadastro()
    return render_template('profile.html', form2 = form2)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))


"""

    query
        INSERT INTO UEA_ALUNO(alu_matricula,alu_nome,alu_endereco, alu_bairro,alu_cidade, alu_UF,alu_CEP,alu_email,alu_telefone,alu_celular,alu_senha) VALUES("1234", "boty", "rua4", "RSPinto", "Manaus", "AM", "6000999", "boty@gmail.com", "852963", "98526487", "btnl");
    C
    x = User(?,?,?,?)
    db.session.add(x)
    db.session.commit()

    R
    r = User.querry.filter_by(nome = "qlqr nome").all()
    print r.username,r.name, r.email             .first()

    U
    x = User.querry.filter_by(nome = "qlqr nome").all()
    x.nome = "Qlqr outro nome"
    db.session.add(x)
    db.session.commit()

    D
    x = User.querry.filter_by(nome = "qlqr nome").all()
    db.session.delete(x)
    db.session.commit()
"""
