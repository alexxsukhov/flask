from flask import Flask, render_template

app = Flask(__name__)

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
        "description": "Отличные кеды, подойдут любому, только выберите размер",
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


@app.route('/')
def index():  # put application's code here
    return render_template("index.html")


@app.route('/catalog/')
def catalog():  # put application's code here
    context = {
        "categories": categories,
    }

    return render_template("catalog.html", **context)


@app.route('/catalog/<slug_category>/')
def page_category(slug_category):  # put application's code here
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


@app.route('/product/<slug_product>/')
def page_product(slug_product):  # put application's code here
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


if __name__ == '__main__':
    app.run(debug=True)
