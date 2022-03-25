from App.models import crops
from App.database import db

def get_all_crops():
    return Crop.query.all()

def create_crop(name, quantity, price):
    newcrop = Crop(name=name, quantity=quantity, price=price)
    db.session.add(newcrop)
    db.session.commit()

def get_all_crops_json():
    crops = Crop.query.all()
    if not crops:
        return []
    crops = [crop.toDict() for crop in crops]
    return crops