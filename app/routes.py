from flask import Blueprint, render_template, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash

from app import db
from app.models import User, Booking
from app.forms import RegisterForm, LoginForm, BookingForm

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return render_template("index.html")


# ---------------- REGISTER ---------------- #

@main.route("/register", methods=["GET", "POST"])
def register():

    form = RegisterForm()

    if form.validate_on_submit():

        existing_user = User.query.filter_by(
            email=form.email.data
        ).first()

        if existing_user:
            return "<h2>Email already registered!</h2>"

        user = User(
            username=form.username.data,
            email=form.email.data,
            password=generate_password_hash(form.password.data)
        )

        db.session.add(user)
        db.session.commit()

        return redirect(url_for("main.login"))

    return render_template(
        "register.html",
        form=form
    )


# ---------------- LOGIN ---------------- #

@main.route("/login", methods=["GET", "POST"])
def login():

    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(
            email=form.email.data
        ).first()

        if user and check_password_hash(
            user.password,
            form.password.data
        ):

            session["user_email"] = user.email

            return redirect(url_for("main.booking"))

        return "<h2>Invalid Email or Password</h2>"

    return render_template(
        "login.html",
        form=form
    )


# ---------------- BOOKING ---------------- #

@main.route("/booking", methods=["GET", "POST"])
def booking():

    if "user_email" not in session:
        return redirect(url_for("main.login"))

    form = BookingForm()

    if form.validate_on_submit():

        booking = Booking(
            user_email=session["user_email"],
            destination=form.destination.data,
            travel_date=form.travel_date.data,
            people=form.people.data
        )

        db.session.add(booking)
        db.session.commit()
        flash("Booking completed successfully!", "success")

        return redirect(url_for("main.my_bookings"))

    return render_template(
        "booking.html",
        form=form
    )


# ---------------- MY BOOKINGS ---------------- #

@main.route("/my-bookings")
def my_bookings():

    if "user_email" not in session:
        return redirect(url_for("main.login"))

    bookings = Booking.query.filter_by(
        user_email=session["user_email"]
    ).all()

    return render_template(
        "my_bookings.html",
        bookings=bookings
    )


# ---------------- LOGOUT ---------------- #

@main.route("/logout")
def logout():

    session.pop("user_email", None)

    return redirect(url_for("main.home"))

@main.route("/cancel-booking/<int:booking_id>")
def cancel_booking(booking_id):

    if "user_email" not in session:
        return redirect(url_for("main.login"))

    booking = Booking.query.filter_by(
        id=booking_id,
        user_email=session["user_email"]
    ).first_or_404()

    db.session.delete(booking)
    db.session.commit()

    flash("Booking cancelled successfully!", "success")

    return redirect(url_for("main.my_bookings"))