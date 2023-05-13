from .db import DB

CLIENTS = DB.collection("clients")

def list_clients():
    return [i.id for i in CLIENTS.stream()]

def new_client(name, email, password):
    """Creates a new client object in the database"""
    CLIENTS.document(email).set({
        "name": name,
        "email": email,
        "password": password,
        "following": []
    })

def update_client(email, data):
    """Updates a client object of the database"""
    CLIENTS.document(email).update(data)
    
def delete_client(email):
    """Deletes a client object of the database"""
    CLIENTS.document(email).delete()
    
def get_client(email):
    """Gets all the data of a client object of the database"""
    return CLIENTS.document(email).get().to_dict()

