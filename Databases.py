from peewee import *
from os import path

ROOT = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(ROOT,"users.db"))

class User(Model):
    names = CharField()
    username = CharField()
    style = CharField()
    email = CharField(unique=True)
    password = CharField()
    class Meta:
        database = db

class Profile(Model):
    username = User.username
    names = User.names
    email = User.email
    style = User.style
    class Meta:
        database = db


User.create_table(fail_silently=True)
Profile.create_table(fail_silently=True)
