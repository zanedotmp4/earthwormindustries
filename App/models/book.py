from App.database import db
from App.models import Donator

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    author = db.Column(db.String)
    publisher = db.Column(db.String)
    pubYear = db.Column(db.Integer)
    edition = db.Column(db.String)
    donatorID = db.Column(db.Integer, db.ForeignKey('donator.id'))

    def toDict(self):
        return{
            'id': self.id,
            'name': self.name,
            'author': self.author,
            'publisher': self.publisher,
            'pub_year': self.pub_year, 
            'edition': self.edition,
            'donatorID': self.donatorID
        }