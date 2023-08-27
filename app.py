from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template("index.html")


@app.route('/catalog/')
def catalog():  # put application's code here
    context = {
        "title": "Каталог одежды и обуви",
        "categories": [
            {
                "name": "Обувь",
                "slug": "shoes",
                "img": "/static/images/shoes.jpg",
            },
            {
                "name": "Одежда",
                "slug": "cloth",
                "img": "/static/images/vidy-kurtok.jpg",
            }
        ],
    }

    return render_template("catalog.html", **context)


@app.route('/catalog/shoes/')
def category_shoes():  # put application's code here
    context = {
        "title": "Обувь",
        "products": [
            {
                "name": "Кеды",
                "slug": "sneakers",
                "img": "/static/images/shoes.jpg",
            },
            {
                "name": "Кеды",
                "slug": "sneakers",
                "img": "/static/images/shoes.jpg",
            },
            {
                "name": "Кеды",
                "slug": "sneakers",
                "img": "/static/images/shoes.jpg",
            },
        ],
    }

    return render_template("category.html", **context)


@app.route('/catalog/cloth/')
def category_cloth():  # put application's code here
    context = {
        "title": "Каталог одежды и обуви",
        "products": [
            {
                "name": "Куртка мужская",
                "slug": "jacket",
                "img": "/static/images/jacket.webp",
            },
            {
                "name": "Куртка мужская",
                "slug": "jacket",
                "img": "/static/images/jacket.webp",
            },
            {
                "name": "Куртка мужская",
                "slug": "jacket",
                "img": "/static/images/jacket.webp",
            },
        ],
    }

    return render_template("category.html", **context)


@app.route('/product/jacket/')
def product_jacket():  # put application's code here
    context = {
        "title": "Куртка мужская",
        "name": "Куртка мужская",
        "slug": "jacket",
        "img": "/static/images/jacket.webp",
        "price": "10000",
        "count": "100",
        "description": "<p>Куртка классная и прекрасная, покупай! Слякоть ни по чем, дождь остается в стороне!</p>",
    }

    return render_template("product.html", **context)


@app.route('/product/sneakers/')
def product_sneakers():  # put application's code here
    context = {
        "title": "Кеды",
        "name": "Кеды",
        "slug": "jacket",
        "img": "/static/images/shoes.jpg",
        "price": "5000",
        "count": "100",
        "description": "Кеды классные и прекрасные, покупай! Слякоть ни по чем, дождь остается в стороне!"
    }

    return render_template("product.html", **context)




if __name__ == '__main__':
    app.run()
