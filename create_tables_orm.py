import os

from flask import Flask, request, render_template
from models import *

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


def main():
    """Create tables"""
    db.create_all()

    """ Update table"""
    # id = 3
    # b = Book.query.get(id)
    # b.title = "Muhammad" 
    # db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        main()