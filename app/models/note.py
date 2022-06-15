from app.config.monfig import db
import datetime
from app.models.user import User
from bson.objectid import ObjectId
from flask import session


class List(list):
    def append(self):
        self.push


class Note:
    def __init__(self, data: dict):

        self.title = data['title']
        self.content = data['content']
        self.created_at = datetime.datetime.now()

    @classmethod
    def append_note(cls, data: dict):
        user_id = {
            '_id': ObjectId(session['current_user'])
        }

        user = User.get_user(user_id)
        print(user)
        user.notes.append(cls(data))
        return user
