from App.models import Client
from App.database import db

def get_all_clients():
    return Client.query.all()

def create_client(fName, lName, address, contact, email):
    newclient = Client(fName=fName, lName=lName, address=address, contact=contact, email=email)
    db.session.add(newclient)
    db.session.commit()

def get_all_clients_json():
    clients = Client.query.all()
    if not clients:
        return []
    clients = [client.toDict() for client in clients]
    return clients