from .db import db


class Admin(db.Document):
    email=db.StringField(required=True)
    username=db.StringField(required=True)
    password=db.StringField(required=True)


class Rooms(db.Document):

    r_number=db.IntField(required=True)
    r_type=db.StringField(required=True)
    r_price=db.IntField(required=True)
    r_status=db.StringField(required=True)


class Complains(db.Document):
    name=db.StringField(required=True)
    email=db.StringField(required=True)
    message=db.StringField(required=True)


class Guests(db.Document):
    g_name = db.StringField(required=True)
    g_email = db.StringField(required=True)
    g_city = db.StringField()
    g_state = db.StringField()
    g_country = db.StringField()
    g_PN = db.IntField()

class bookings(db.Document):
    at = db.DateTimeField(required=True)
    dt = db.DateTimeField(required=True)
    g_name = db.StringField()
    r_count = db.IntField()
    bill = db.IntField()