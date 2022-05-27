from app.config.monfig import db
from datetime import datetime as date

class User:
    def __init__(self, data: dict) -> None:
        self.id = data['_id']
        self.name = data['name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = date.datetime.now()