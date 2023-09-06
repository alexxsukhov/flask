from flask import Flask, render_template, make_response, request, redirect, flash, url_for
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from forms import RegisterForm, AuthForm

app = Flask(__name__)
app.secret_key = b'0c89b93b34c40a0884814697a2005e154487bae8019e7d5d5b54fb123dc91f89'
app.config['SECRET_KEY'] = '0c89b93b34c40a0884814697a2005e154487bae8019e7d5d5b54fb123dc91f89'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
csrf = CSRFProtect(app)

users = [
    {
        "login": "fr-man",
        "password": "qwerty",
        "email": "mail@mail.com",
    }
]

categories = [
    {
        "id": 1,
        "name": "Обувь",
        "announce": "Обувь для всей семьи",
        "slug": "shoes",
        "img_src": "/static/images/shoes.jpg",
    },
    {
        "id": 2,
        "name": "Одежда",
        "slug": "cloth",
        "announce": "Одежда для всей семьи",
        "img_src": "/static/images/cloth.jpg",
    },
]

products = [
    {
        "id": 1,
        "category_id": 1,
        "name": "Кеды",
        "announce": "Кеды для всей семьи",
        "slug": "shoes",
        "price": "5000",
        "img_src": "/static/images/shoes.jpg",
        "description": "Отличные кеды",
    },
    {
        "id": 2,
        "category_id": 2,
        "name": "Куртка",
        "announce": "Великолепие",
        "slug": "jacket",
        "price": "5000",
        "img_src": "/static/images/jacket.webp",
        "description": "Хорошая куртка",
    },
]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/catalog/")
def catalog():
    context = {
        "categories": categories,
    }

    return render_template("catalog.html", **context)


@app.route("/catalog/<slug_category>/")
def page_category(slug_category):
    for category in categories:

        if category["slug"] == slug_category:
            products_list = []
            for product in products:
                if product["category_id"] == category["id"]:
                    products_list.append(product)
            context = {
                "category": category,
                "products": products_list,
            }
            return render_template("category.html", **context)
    else:
        return render_template("404.html")


@app.route("/product/<slug_product>/")
def page_product(slug_product):
    for product in products:
        if product["slug"] == slug_product:
            context = {
                "name": product["name"],
                "price": product["price"],
                "img": product["img_src"],
                "description": product["description"],
            }

            return render_template("product.html", **context)
    else:
        return render_template("404.html")


@app.route("/auth/", methods=["GET", "POST"])
def auth():
    form = AuthForm()
    if request.method == "POST" and form.validate():
        usr_login = form.usr_login.data
        usr_password = form.usr_password.data
        for user in users:
            if usr_password == user["password"] and usr_login == user["login"]:
                response = make_response(redirect("/welcome/"))
                response.set_cookie("logged", "yes")
                response.set_cookie("login", usr_login)
                return response
            else:
                flash('Неправильный логин или пароль! Попробуйте еще раз!', 'danger')
    return render_template('auth.html', form=form)


@app.route('/logout/')
def logout():
    response = make_response(redirect(url_for("auth")))
    response.delete_cookie('logged')
    response.delete_cookie('login')
    return response


@app.route("/welcome/")
def welcome():
    logged = request.cookies.get('logged')
    login = request.cookies.get('login')
    context = {
        "login": login,
    }
    if logged:
        return render_template('welcome.html', **context)
    else:
        return redirect(url_for("auth"), 303)


@app.route("/registration/", methods=["GET", "POST"])
def registration():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        pass

    return render_template('registration.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
