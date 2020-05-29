class Author:
     
    def __init__(self, name):
         self.name = name
    
    def __repr__(self):
        return self.name

         
class Book:

    def __init__(self, isbn, title, author, year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year

    def print_info(self):
        print(f"isbn: {self.isbn}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year: {self.year}")
        

def main():
    
    a1 = Author("Raymond E. Feist")
    b1 = Book(isbn="0380795272", title="Krondor: The Betrayal", author=a1, year=1990)
    b1.print_info()

    print()
    
    a2 = Author("Susan Cooper")
    b2 = Book(isbn="1416949658", title="The Dark Is Rising",author=a2, year=1973)
    b2.print_info()


if __name__ == "__main__":
    main()