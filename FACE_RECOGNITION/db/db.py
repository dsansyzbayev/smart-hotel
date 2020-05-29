from mongoengine import *


def db_conn():
    connect("smart_shop")
