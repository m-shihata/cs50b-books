import os

from flask import Flask, request, render_template, json
from models import *

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():

    # Prompt user to choose a flight
    # print("This application will help you search for a book using it's title or the author's name..")
    s = input("Search for: ")

    books = db.session.query(Author, Book).filter(Author.id ==
    Book.author_id).filter(Book.title.like(f"%{s}%") | Author.name.like(f"%{s}%")).all()

    # Make name is valid.
    if len(books) == 0:
        print("Error: No such a book.")
        return

    for book in books:
        print("title: " + book[1].title + ", Author: " + book[0].name)
       
    
if __name__ == "__main__":
    with app.app_context():
        main()