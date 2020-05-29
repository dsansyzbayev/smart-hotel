from mongoengine import *


class UserPhoto(Document):
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    phone_number = StringField(required=True, unique=True)
    img_encoding = ListField(FloatField())


class Reservation(Document):
    hotel_name = StringField(required=True)
    user_phone_number = StringField(required=True, unique=True)
    beginning_date = DateTimeField(required=True)
    ending_date = DateTimeField(required=True)
