from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField,
                     BooleanField, SelectField, DateField,
                     IntegerField, DecimalField, FileField)
from wtforms.validators import DataRequired, Email, EqualTo


class RegisterForm(FlaskForm):
    usr_login = StringField('Login',
                            validators=[DataRequired()],
                            render_kw={"placeholder": "Введите Ваш логин", "class": "form-control"})
    email = StringField('Email',
                        validators=[DataRequired(), Email(message="Введен не Email")],
                        render_kw={"placeholder": "Введите Ваш email", "class": "form-control"})
    usr_password = PasswordField('Password',
                                 validators=[DataRequired()],
                                 render_kw={"placeholder": "Введите пароль", "class": "form-control"})
    usr_password_confirm = PasswordField('Confirm Password',
                                         validators=[DataRequired(),
                                                     EqualTo('usr_password', message="Пароли не совпадают")],
                                         render_kw={"placeholder": "Повторите пароль", "class": "form-control"})


class AuthForm(FlaskForm):
    usr_login = StringField('Логин', validators=[DataRequired()],
                            render_kw={"placeholder": "Введите Ваш логин", "class": "form-control"})
    usr_password = PasswordField('Пароль', validators=[DataRequired()],
                                 render_kw={"placeholder": "Введите пароль от логина", "class": "form-control"})
