from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from mypinterest.models import User


class FormLogin(FlaskForm):
    email = StringField("e-mail", validators=[DataRequired(), Email()])
    password = PasswordField("password", validators=[DataRequired()])
    btn = SubmitField("login")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if not user:
            raise ValidationError("User not found, create an account.")


class FormCreateUser(FlaskForm):
    email = StringField("e-mail", validators=[DataRequired(), Email()])
    username = StringField("username", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired(), Length(5, 12)])
    check_password = PasswordField("confirm password", validators=[DataRequired(), EqualTo("password")])
    btn = SubmitField("create account")

    # Validaçao de email unico .

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("Email already registered, log in to continue.")


class FormPicture(FlaskForm):
    picture = FileField("Picture", validators=[DataRequired()])
    btn = SubmitField("Send")















