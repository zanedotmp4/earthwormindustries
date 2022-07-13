from App.database import db

class Donator(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fName = db.Column(db.String, nullable=False)
    lName = db.Column(db.String, nullable=False)
    address = db.Column(db.String)
    contact = db.Column(db.Integer)
    email = db.Column(db.String)

    def toDict(self):
        return{
            'id': self.id,
            'fname': self.fname,
            'lname': self.lname,
            'address': self.address,
            'contact': self.contact, 
            'email': self.email
        }