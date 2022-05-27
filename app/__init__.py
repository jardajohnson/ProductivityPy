from flask import Flask, session, flash, redirect, render_template
from flask_bcrypt import Bcrypt


app = Flask(__name__)

app.secret_key = "abc"
bcrypt = Bcrypt(app)
