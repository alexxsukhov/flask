from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField,
                     BooleanField, SelectField, DateField,
                     IntegerField, DecimalField, FileField)
from wtforms.validators import DataRequired, Email, EqualTo


class RegisterForm(FlaskForm):
    usr_login = StringField('Login',
                            validators=[DataRequired()],
                            render_kw={"placeholder": "Введите Ваш логин", "class": "form-control"})
    usr_password = PasswordField('Password',
                                 validators=[DataRequired()],
                                 render_kw={"placeholder": "Введите пароль", "class": "form-control"})
    usr_password_confirm = PasswordField('Password',
                                         validators=[DataRequired()],
                                         render_kw={"placeholder": "Повторите пароль", "class": "form-control"})
    gender = SelectField('Gender',
                         choices=[
                             ('male', 'Мужчина'),
                             ('female', 'Женщина')
                         ],
                         render_kw={"placeholder": "Выберите пол", "class": "form-select"}
                         )


class AuthForm(FlaskForm):
    usr_login = StringField('Логин', validators=[DataRequired()],
                            render_kw={"placeholder": "Введите Ваш логин", "class": "form-control"})
    usr_password = PasswordField('Пароль', validators=[DataRequired()],
                                 render_kw={"placeholder": "Введите пароль от логина", "class": "form-control"})
