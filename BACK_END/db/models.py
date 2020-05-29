from db.db import db


class UserPhoto(db.Document):
    first_name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    phone_number = db.StringField(required=True, unique=True)
    img_encoding = db.ListField()


class User(db.Document):
    first_name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    phone_number = db.StringField(required=True, unique=True)
    card_number = db.StringField(required=True, unique=True)
    login = db.StringField(required=True, unique=True)
    password = db.StringField(required=True)


class Hotel(db.Document):
    name = db.StringField(required=True, unique=True)
    price = db.DecimalField(min_value=0.0, required=True)


class Reservation(db.Document):
    hotel_name = db.StringField(required=True)
    user_phone_number = db.StringField(required=True, unique=True)
    beginning_date = db.DateTimeField(required=True)
    ending_date = db.DateTimeField(required=True)
