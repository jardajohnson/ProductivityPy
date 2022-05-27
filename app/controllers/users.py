from flask import render_template, request, redirect, flash, session
from bson.objectid import ObjectId

from app import app, bcrypt

from app.models.user import User


@app.route('/')
def dashboard():
    if not 'current_user' in session:
        return render_template('dashboard.html')

    data = {
        '_id': ObjectId(session['current_user'])
    }
    current_user = User.get_user(data)

    return render_template('dashboard.html', user=current_user)


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

    current_user = User.save(data)
    session['current_user'] = current_user

    return redirect('/')
