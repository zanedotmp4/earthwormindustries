from App.database import db

class Livestock(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name =  db.Column(db.String(255), nullable=False)
  quantity = db.Column(db.Integer)
  price = db.Column(db.Double)
  noOfAdults = db.Column(db.Integer)
  noOfYoung = db.Column(db.Integer)

  def toDict(self):
    return {
      'id': salf.id,
      'name': self.name,
      'quantity': self.quantity,
      'price': self.price,
      'noOfAdults': self.noOfAdults,
      'noOfYoung': self.noOfYoung
    }

  