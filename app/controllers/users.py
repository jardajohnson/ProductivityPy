from flask import render_template, request, redirect, flash, session
from app import app, bcrypt
from pprint import pprint
from app.models.user import User


@app.route('/')
def dashboard():
    if not 'current_user' in session:
        return render_template('dashboard.html')
    
    return render_template('dashboard.html')

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
