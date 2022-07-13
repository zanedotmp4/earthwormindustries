from App.models import Quantity
from App.models import Book
from App.database import db

def get_all_quantities():
    return Quantity.query.all()

def create_quantity(bookID, amtOwned, amtAvail, amtLoaned):
    newamt = Quantity(bookID=bookID, amtOwned=amtOwned, amtAvail=amtAvail, amtLoaned=amtLoaned)
    db.session.add(newamt)
    db.session.commit()

def get_all_quantities_json():
    amts = Quantity.__query.all()
    if not amts:
        return []
    amts = [quantity.toDict() for quantity in amts]
    return amts