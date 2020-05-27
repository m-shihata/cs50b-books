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

    books = db.session.query(Author, Book).filter(Author.id ==
                Book.author_id).filter(Book.title.like(f"%{s}%") | Author.name.like(f"%{s}%")).all()

    # Make sure flight is valid.
    if len(books) == 0:
        return render_template("error.html", message="No results found")

    return render_template("books.html", books=books)


@app.route("/book/<int:book_id>")
def book(book_id):
    book = Book.query.get(book_id)
    author = book.author
    return render_template("book.html", book=book, author=author)


