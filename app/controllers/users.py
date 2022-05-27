from flask import render_template, request, redirect, flash, session
from app import app
from pprint import pprint
from app.models.user import User


@app.route('/')
def dashboard():
    return render_template('dashboard.html')


@app.route('/user/new', methods=['POST'])
def handle_new_user():

    if not User.validate_user(request.form):
        return redirect('/')
    return redirect('/')
