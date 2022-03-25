from App.database import db

listing = db.Table('listing',                db.Column('listingID',db.Integer,primary_key=True),
db.Column('cropId', db.Integer, db.ForeignKey('crop.id')),
db.Column('livestockID',db.Integer,db.ForeignKey('livestock.id'))
)