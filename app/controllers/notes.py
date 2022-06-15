from app.models.note import Note
from app import app
from flask import render_template, request, session, redirect


@app.route('/note/new', methods=['POST'])
def create_note():

    if not 'current_user' in session:
        return redirect('/')
    data = {
        'title': request.form['title'],
        'content': request.form['content'],

    }
    Note.append_note(data)

    return redirect('/')
