from App.database import db
from App.models import Book

class Quantity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bookID = db.Column(db.Integer, db.ForeignKey('book.id'))
    amtOwned = db.Column(db.Integer)
    amtAvail = db.Column(db.Integer)
    amtLoaned = db.Column(db.Integer)

    def toDict(self):
        return{
            'id': self.id,
            'bookID': self.bookID,
            'amtOwned': self.amtOwned,
            'amtAvail': self.amtAvail,
            'amtLoaned': self.amtLoaned
        }