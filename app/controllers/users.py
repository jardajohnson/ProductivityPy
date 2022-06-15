from flask import render_template, request, redirect, flash, session
from bson.objectid import ObjectId
import random
from app import app, bcrypt

from app.models.user import User
from app.models.quote import Quote


@app.route('/')
def dashboard():
    quotes = Quote.make_quotes()
    print(quotes)
    quote = random.choice(quotes)
    if not 'current_user' in session:
        return render_template('dashboard.html', quote=quote)

    data = {
        '_id': ObjectId(session['current_user'])
    }
    current_user = User.get_user(data)
    print(type(current_user.notes))
    return render_template('dashboard.html', user=current_user, quote=quote)


@app.route('/user/new', methods=['POST'])
def handle_new_user():

    if not User.validate_user(request.form):
        return redirect('/')

    hash = bcrypt.generate_password_hash(request.form['password'])

    data = {
        'name': request.form['name'],
        'email': request.form['email'],
        'password': hash
    }

    current_user = User.create_user(data)
    session['current_user'] = str(current_user)

    return redirect('/')


@app.route('/login', methods=['POST'])
def handle_login():

    data = {
        'email': request.form['email'],
    }
    result = User.get_user(data)

    if not result:
        flash("Invalid email/password, Please try again", 'login')
        return redirect('/')
    if not bcrypt.check_password_hash(result.password, request.form['password']):
        flash("Invalid email/password, Please try again", 'login')
        return redirect('/')
    session['current_user'] = str(result.id)
    return redirect('/')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
