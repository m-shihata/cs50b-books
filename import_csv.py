import csv
import os 

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

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

        if index == 0:
            continue

        year = int(year)

        """ Add the author to authors table if it's not already there """
        if author not in authors:
        
            # Rigure out the author ID
            authors[author] = len(authors) + 1

            # Execute the insertion 
            db.execute("INSERT INTO authors (name) VALUES (:name)", {"name": author})

            # Print what happend for me 
            print(f"{author} the author of {title} is added to authors table with id = {len(authors)}")

        else:
            # Do nothing but print already exists statement for me 
            print(f"Author already exists in authors table with id: {authors[author]}")


        """ Add the book to the books table """

        # Execute the insertion  
        db.execute('INSERT INTO books (isbn, title, author_id, year) VALUES (:isbn, :title, :author_id, :year)', 
                    {"isbn": isbn, "title": title, "author_id": authors[author], "year": year})

        # Print what happend for me 
        print(f"({isbn}, {title}, {authors[author]}, {year}) inserted into books table")
    
    db.commit()
    

if __name__ == "__main__":
    main()