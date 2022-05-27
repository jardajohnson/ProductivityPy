from flask import Flask, session, flash, redirect, render_template

app = Flask(__name__)

app.secret_key = "abc"
