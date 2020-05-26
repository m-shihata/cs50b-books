import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():

    # Prompt user to choose a flight
    print("This application will help you search for a book using it's title or the author's name..")
    search_input = input("Search for: ")

    books = db.execute("SELECT isbn, title, name, year FROM books INNER JOIN authors ON author_id = authors.id WHERE title LIKE :search_input OR name LIKE :search_input;",
                        {"search_input": f"%{search_input}%"}).fetchall()

    # Make sure flight is valid.
    if len(books) == 0:
        print("Error: No such a book.")
        return

    for book in books:
        print(book.title)

if __name__ == "__main__":
    main()