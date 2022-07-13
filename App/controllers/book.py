from App.models import Book
from App.models import Donator
from App.database import db

def get_all_books():
    return Book.query.all()

def create_book(name, author, publisher, pubYear, edition, donatorID):
    newbook = Book(name=name, author=author, publisher=publisher, pubYear=pubYear, edition=edition, donatorID=donatorID)
    db.session.add(newbook)
    db.session.commmit()

def get_all_books_json():
    books = Book.query.all()
    if not books:
        return []
    books = [book.toDict() for book in books]
    return books