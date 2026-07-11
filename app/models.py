from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(100), nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    password = db.Column(db.String(255), nullable=False)


class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    user_email = db.Column(db.String(120), nullable=False)

    destination = db.Column(db.String(100), nullable=False)

    travel_date = db.Column(db.String(50), nullable=False)

    people = db.Column(db.Integer, nullable=False)