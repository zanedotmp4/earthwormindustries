from App.models import Loan
from App.models import Book
from App.models import Client
from App.database import db

def get_all_loans():
    return Loan.query.all()

def create_loan(bookID, clientID, loanDate, returnDate):
    newloan = Loan(bookID=bookID, clientID=clientID, loanDate=loanDate, returnDate=returnDate)
    db.session.add(newloan)
    db.session.commit()

def get_all_loans_json():
    loans = Loan.query.all()
    if not loans:
        return []
    loans = [loan.toDict() for loan in loans]
    return loans