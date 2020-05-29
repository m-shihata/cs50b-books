import os

from flask import Flask, request, render_template
from models import *
from helpers import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/books", methods=["POST"])
def books():
    
    s = get("search_input")

    if not get("search_input"):
        return render_template("error.html", message="You must type something!")

    books = Book.query.filter(Book.title.like(f"%{s}%")).order_by(Book.title).all()
    authors = Author.query.filter(Book.title.like(f"%{s}%")).order_by(Author.name).all()

    # Make sure flight is valid.
    if len(books) == 0 and len(authors) == 0:
        return render_template("error.html", message="No results found")

    return render_template("books.html", books=books, authors=authors)


@app.route("/book/<int:book_id>")
def book(book_id):
    book = Book.query.get(book_id)
    author = book.author
    return render_template("book.html", book=book, author=author)


@app.route("/author/<int:author_id>")
def author(author_id):
    author = Author.query.get(author_id)
    books = Book.query.filter_by(author_id = author_id).order_by(Book.title).all()
    return render_template("author.html", author=author, books=books)


