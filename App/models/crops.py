from App.database import db

class Crop(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name =db.Column(db.String(255), nullable =False)
  price = db.Column(db.Double nullable = False)
  quantity =db.Column(db.Integer, nullable = False)
  status = db.Column(db.String(80),nullable=False)

  def toDict(self):
    return{
      'id':self.id,
      'name':self.name,
      'price':self.price,
      'quantity':self.quantity,
      'status':self.status
    }
  
