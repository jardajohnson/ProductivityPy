from flask import render_template, request, redirect, flash, session
from app import app


@app.route('/')
def dashboard():
    return render_template('dashboard.html')
