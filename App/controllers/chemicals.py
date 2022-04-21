from App.models import chemicals
from App.database import db

def get_all_chemicals():
    return Chemical.query.all()

def create_chemical(name, quantity,npk1,npk2,npk3):
    newchemical = Chemical(name=name, quantity=quantity,npk1=npk1,npk2=npk2,npk3=npk3)
    db.session.add(newchemical)
    db.session.commit()

def get_all_chemicals_json():
    chemicals = Chemical.query.all()
    if not chemicals:
        return []
    chemicals = [chemical.toDict() for chemical in chemicals]
    return crops
