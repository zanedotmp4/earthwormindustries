from App.models import livestock
from App.database import db

def get_all_livestock():
    return Livestock.query.all()

def create_livestock(name, quantity, price):
    newls = Livestock(name=name, quantity=quantity, price=price)
    db.session.add(newls)
    db.session.commit()

def get_all_livestock_json():
    ls = Livestock.query.all()
    if not ls:
        return []
    ls = [livestock.toDict() for livestock in ls]
    return ls