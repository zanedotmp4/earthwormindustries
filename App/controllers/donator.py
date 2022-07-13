from App.models import Donator
from App.database import db

def get_all_donators():
    return Donator.query.all()

def create_donator(fName, lName, address, contact, email):
    newdon = Donator(fName=fName, lName=lName, address=address, contact=contact, email=email)
    db.session.add(newdon)
    db.session.commit()

def get_all_donators_json():
    donators = Donator.query.all()
    if not donators:
        return []
    donators = [donator.toDict() for donator in donators]
    return donators