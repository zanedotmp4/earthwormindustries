from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
# from App.models import listing
from flask_login import UserMixin

class Listing(db.Model):
    id = db.Column(db.Integer, primary_key=True)

listings = db.Table('listings',
    db.Column('crop_id', db.Integer, db.ForeignKey('crop.id'), primary_key=True),
    db.Column('livestock_id', db.Integer, db.ForeignKey('livestock.id'), primary_key=True),
    db.Column('chemical_id', db.Integer, db.ForeignKey('chemical.id'), primary_key=True)
)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    # listings = db.relationship('Listing', secondary=listings, lazy='subquery', backref=db.backref('users', lazy=True))
    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def toDict(self):
        return{
            'id': self.id,
            'username': self.username
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

