#تراكيب البيانات - التحدي الأول
#الحل من موقع هرمش مع بعض التعديلات السطحية

class Author:
    __id_incrementer = 0

    def __init__(self, name, phone, email):
        Author.__id_incrementer += 1
        self.id = Author.__id_incrementer
        self.name = name
        self.phone = phone
        self.email = email


class Book:
    __id_incrementer = 0

    def __init__(self, title, publishing_date, version, author):
        Book.__id_incrementer += 1
        self.id = Book.__id_incrementer
        self.title = title
        self.publishing_date = publishing_date
        self.verdion = version
        self.author = author


class Library:
    authors = []
    books = []

    def add_author(self, Author):
        self.authors.append(Author)

    def remove_author(self, id):
        for Author in self.authors:
            if Author.id == id:
                self.authors.remove(Author)
                return
        print("Author with id", id, "is not found!")
        print("----------------------")

    def print_author(self, id):
        for Author in self.authors:
            if Author.id == id:
                print("Author with id", id, "informations:")
                print("Name:", Author.name)
                print("Phone:", Author.phone)
                print("Email", Author.email)
                print("----------------------")
                return
        print("Author with id", id, "is not found!")
        print("----------------------")

    def print_author_books(self, id):
        is_author_exist = False
        author_name = ''
        for Author in self.authors:
            if Author.id == id:
                is_author_exist = True
                author_name = Author.name
                break

        if not is_author_exist:
            print("Author with id", id, "is not found!")
            print("----------------------")
            return

        print("Books of author " + author_name + ":")
        for book in self.books:
            if book.author.id == id:
                print("- " + book.title)
        print("----------------------")

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, id):
        for book in self.books:
            if book.id == id:
                self.books.remove(book)
                return

        print("Book with id", id, "is not found!")
        print("----------------------")

    def print_book(self, id):
        for book in self.books:
            if book.id == id:
                print("Book with id", id, " informations:")
                print("Title:", book.title)
                print("Publishing date:", book.publishing_date)
                print("Author:", book.author.name)
                print("----------------------")
                return
        print("Book with id", id, "is not found!")
        print("----------------------")

#مثال

author1 = Author("Mhamad", "+96170123456", "mhamad@gmail.com")
author2 = Author("Salem", "+9664021833", "salem@gmail.com")
author3 = Author("Rola", "+9631249392", "rola@gmail.com")

book1 = Book("Learn Java", "12-20-2019", 1, author1)
book2 = Book("Learn HTML", "8-5-2018", 3, author1)
book3 = Book("PHP for beginners", "10-2-2019", 1, author2)
book4 = Book("C# for dummies", "12-20-2019", 1, author3)

library = Library()

library.add_author(author1)
library.add_author(author2)
library.add_author(author3)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)

library.print_author(1)
library.print_author(2)
library.print_author(3)

library.print_book(1)
library.print_book(2)
library.print_book(3)
library.print_book(4)

library.print_author_books(1)
library.print_author_books(2)
library.print_author_books(3)

library.remove_author(2)
library.print_author(2)
library.print_author_books(2)

#انتهى
