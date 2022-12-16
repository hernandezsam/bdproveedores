from flask import render_template, request, redirect
from app import app, db
from app.models import Entry

jedi = "of the jedi"

@app.route('/')
@app.route('/index')
def index():
    # entries = [
    #     {
    #         'id' : 1,
    #         'rut': 'test rut 1',
    #         'razon_social' : 'test razon_social 1',
    #         'status' : True
    #     },
    #     {
    #         'id': 2,
    #         'title': 'test title 2',
    #         'description': 'test desc 2',
    #         'status': False
    #     }
    # ]
    entries = Entry.query.all()
    return render_template('index.html', entries=entries)

@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        form = request.form
        rut = form.get('rut')
        razon_social = form.get('razon_social')
        cod_banco = form.get('cod_banco')
        banco = form.get('banco')
        tipo_cta = form.get('tipo_cta')
        num_cta = form.get('num_cta')
        email = form.get('email')
        if not rut or razon_social or cod_banco or banco or num_cta or email :
            entry = Entry(rut = rut, razon_social = razon_social , cod_banco = cod_banco , banco = banco , tipo_cta = tipo_cta, num_cta = num_cta , email = email)
            db.session.add(entry)
            db.session.commit()
            return redirect('/')

    return "of the jedi"

@app.route('/update/<int:id>')
def updateRoute(id):
    if not id or id != 0:
        entry = Entry.query.get(id)
        if entry:
            return render_template('update.html', entry=entry)

    return "of the jedi"

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    if not id or id != 0:
        entry = Entry.query.get(id)
        if entry:
            rut = form.get('rut')
            entry.rut = rut
            razon_social = form.get('razon_social')
            entry.razon_social = razon_social
            cod_banco = form.get('cod_banco')
            entry.cod_banco = cod_banco
            banco = form.get('banco')
            entry.banco = banco
            tipo_cta = form.get('tipo_cta')
            entry.tipo_cta = tipo_cta
            num_cta = form.get('num_cta')
            entry.num_cta = num_cta
            email = form.get('email')
            entry.email = email
            db.session.commit()
        return redirect('/')

    return "of the jedi"



@app.route('/delete/<int:id>')
def delete(id):
    if not id or id != 0:
        entry = Entry.query.get(id)
        if entry:
            db.session.delete(entry)
            db.session.commit()
        return redirect('/')

    return "of the jedi"

@app.route('/turn/<int:id>')
def turn(id):
    if not id or id != 0:
        entry = Entry.query.get(id)
        if entry:
            entry.status = not entry.status
            db.session.commit()
        return redirect('/')

    return "of the jedi"

# @app.errorhandler(Exception)
# def error_page(e):
#     return "of the jedi"