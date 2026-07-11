from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class RegisterForm(FlaskForm):

    username = StringField(
        "Username",
        validators=[DataRequired(), Length(min=3, max=30)]
    )

    email = StringField(
        "Email",
        validators=[DataRequired(), Email()]
    )

    password = PasswordField(
        "Password",
        validators=[DataRequired(), Length(min=6)]
    )

    submit = SubmitField("Register")


class LoginForm(FlaskForm):

    email = StringField(
        "Email",
        validators=[DataRequired(), Email()]
    )

    password = PasswordField(
        "Password",
        validators=[DataRequired()]
    )

    submit = SubmitField("Login")


class BookingForm(FlaskForm):

    destination = StringField(
        "Destination",
        validators=[DataRequired()]
    )

    travel_date = StringField(
        "Travel Date",
        validators=[DataRequired()]
    )

    people = IntegerField(
        "Number of People",
        validators=[DataRequired()]
    )

    submit = SubmitField("Book Trip")