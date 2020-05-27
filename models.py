import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

# class Student(db.Model):
#     __tablename__ = "students"
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String, nullable=False) 


class Author(db.Model):
    __tablename__ = "authors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False) 


class Book(db.Model):
    __tablename__ = "books" 
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("authors.id"), nullable=False)
    author = db.relationship("Author", backref="book", lazy=True)
    # borrowers = db.relationship("Borrower", backref="book", lazy=True)

    # def add_borrower(self, name):
    #     b = Borrower(name=name, book_id=self.id)
    #     db.session.add(b)
    #     db.session.commit()


# class Borrower(db.Model):
#     __tablename__ = "borrowers"
#     student_id = db.Column(db.Integer, db.ForeignKey("students.id"), nullable=False)
#     book_id = db.Column(db.Integer, db.ForeignKey("books.id"), nullable=False)
