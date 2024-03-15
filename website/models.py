from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
import datetime


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    role = db.Column(db.Boolean, default = 0)
    notes = db.relationship('Note')
    budget = db.Column(db.Integer, default = 20)

    def get_budget(self):
        return self.budget
    

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    def __repr__(self):
        return f'Item {self.name}'

    def buy(self, user):
        user.budget -= self.price
        db.session.commit()

class UserItemRelationship(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    item_id = db.Column(db.Integer(), db.ForeignKey('item.id'))
    date_time = db.Column(db.DateTime(timezone=True), default=datetime.datetime.now)