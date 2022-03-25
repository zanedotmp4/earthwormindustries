from App.database import db

listing =db.Table('listing',                db.Column('listingID',db.Interger,primary_key=True),
db.Column('cropId', db.Integer, db.ForeignKey('crop.id')),
db.Column('livestockID',db.Interger,db.ForeignKey('livestock.id'))
)