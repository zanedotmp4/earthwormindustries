from App.database import db

class Chemical(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name =db.Column(db.String(255), nullable =False)
  quantity =db.Column(db.Integer, nullable = False)
  npk1 = db.Column(db.Integer, nullable = False)
  npk2 = db.Column(db.Integer, nullable = False)
  npk3 =db.Column(db.Integer, nullable = False)

  def toDict(self):
      return{
        'id':self.id,
        'name':self.name,
        'quantity':self.quantity,
        'npk1':self.npk1,
        'npk2':self.npk2,
        'npk3':self.npk3
      }