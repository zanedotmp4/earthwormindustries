from App.models import 
from App.database import db

def get_all_chemicals():
    return Chemical.query.all()

def create_chemical(name, quantity, price):
    newchemical = Crop(name=name, quantity=quantity, price=price)
    db.session.add(newchemical)
    db.session.commit()

def get_all_chemicals_json():
    chemicals = Chemical.query.all()
    if not chemicals:
        return []
    chemicals = [chemical.toDict() for chemical in chemicals]
    return crops
