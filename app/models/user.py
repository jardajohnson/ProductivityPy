from flask import flash
from app.config.monfig import db
from datetime import datetime as date
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:
    def __init__(self, data: dict) -> None:
        self.id = data['_id']
        self.name = data['name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = date.datetime.now()
        self.notes = []


# * Static methods

    @staticmethod
    def validate_user(user) -> bool:
        is_valid = True  # we assume this is true

        if len(user['name']) < 2 or not user['name'].isalpha():
            flash(
                "First name must be at least 2 characters, and contain all alphabetic characters.", "register")
            is_valid = False

        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address", "register")
            is_valid = False

        if len(user['password']) < 4:
            flash(
                "Password must be at least 4 characters", "register")
            is_valid = False
        if user['confirm_password'] != user['password']:
            flash("Passwords must match.", "register")
            is_valid = False
        return is_valid

# * Class methods
# ! CREATE

    @classmethod
    def create_user(cls, data: dict) -> int:
        result = db.users.insert_one(data)
        return result.inserted_id
    
# ! READ

    @classmethod
    def get_user(cls, data: dict) -> object:

        result = db.users.find_one(data)
        print('get_one data:', result)
        return cls(result)