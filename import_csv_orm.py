import csv
import os 

from flask import Flask, request, render_template
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


def main():

    # Open csv file 
    f= open("books.csv")

    # Create a reader
    reader = csv.reader(f)

    index = -1
    authors = dict()

    for isbn, title, author, year in reader:

        # index of the row 
        index += 1

        print("{}, {}, {}, {}, {}".format(index, isbn, title, author, year))

        # Pass the table headings
        if index == 0:
            continue

        # Convert year to integer 
        year = int(year)

        # Add the author to authors table if it's not already there 
        if author not in authors:
            authors[author] = len(authors) + 1
            a = Author(name=author)
            db.session.add(a)
            db.session.commit()
        
        # Add the book to the books table 
        b = Book(isbn=isbn, title=title, year=year, author_id=authors[author])
        db.session.add(b)
        db.session.commit()
    

if __name__ == "__main__":
    with app.app_context():
        main()