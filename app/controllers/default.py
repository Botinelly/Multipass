from app import *
from flask import render_template, flash, request, redirect, url_for
from app.models.forms import *
from app.models.tables import User
from flask_login import login_user, logout_user, login_required
from flask import jsonify
from werkzeug.utils import secure_filename

db.create_all()

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@lm.user_loader
def load_user(alu_matricula):
    return User.query.filter_by(alu_matricula=alu_matricula).first()

@app.route("/index", methods=["GET", "POST"])
@app.route("/", methods=["GET", "POST"])
def index():
    form1 = Login()
    if form1.login.data != "" and form1.password.data != ""  and form1.validate_on_submit():
        u = User.query.filter_by(alu_email=form1.login.data).first()
        p = User.query.filter_by(alu_senha=form1.password.data).first()
        if u and p:
            login_user(u)
            return redirect(url_for("home"))
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

@app.route("/profile/<matricula>", methods=["GET", "POST"])
@login_required
def profile(matricula):
    form2 = Cadastro()
    r = User.query.filter_by(alu_matricula = matricula).first()

    form2.matricula.data = r.alu_matricula
    form2.nome.data = r.alu_nome
    form2.endereco.data = r.alu_endereco
    form2.bairro.data = r.alu_bairro
    form2.cidade.data = r.alu_cidade
    form2.UF.data = r.alu_UF
    form2.CEP.data = r.alu_CEP
    form2.email.data = r.alu_email
    form2.telefone.data = r.alu_telefone
    form2.celular.data = r.alu_celular
    form2.senha.data = r.alu_senha

    if form2.matricula.data != "" and form2.nome.data != "" and form2.endereco.data != "" and form2.bairro.data != "" and form2.cidade.data != "" and form2.UF.data != "" and form2.CEP.data != "" and form2.email.data != "" and form2.telefone.data != "" and form2.celular.data != "" and form2.validate_on_submit():
        form2 = Cadastro()
        r.alu_matricula = form2.matricula.data
        r.alu_nome = form2.nome.data
        r.alu_endereco = form2.endereco.data
        r.alu_bairro = form2.bairro.data
        r.alu_cidade = form2.cidade.data
        r.alu_UF = form2.UF.data
        r.alu_CEP = form2.CEP.data
        r.alu_email = form2.email.data
        r.alu_telefone = form2.telefone.data
        r.alu_celular = form2.celular.data
        r.alu_senha = form2.senha.data

        db.session.add(r)
        db.session.commit()

        return redirect(url_for('home'))
    return render_template('profile.html', form2 = form2)

@app.route("/api_user/<matricula>", methods=["GET"])
@login_required
def api_user(matricula):
    result = User.query.filter_by(alu_matricula = matricula).first()
    return jsonify(username = result.alu_nome, matricula = result.alu_matricula, endereco = result.alu_endereco)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/teste", methods=["GET", "POST"])
def teste():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('teste'))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

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
