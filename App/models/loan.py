from App.database import db
from App.models import Book
from App.models import Client

class Loan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bookID = db.Column(db.Integer, db.ForeignKey('book.id'))
    clientID = db.Column(db.Integer, db.ForeignKey('client.id'))
    loanDate = db.Column(db.Date, nullable=False)
    returnDate = db.Column(db.Date)

    def toDict(self):
        return{
            'id': self.id,
            'bookID': self.bookID,
            'clientID': self.clientID,
            'loanDate': self.loanDate,
            'returnDate': self.returnDate
        }