from db import DB

CLIENTS = DB.collection("clients")

def list_clients():
    return [i.id for i in CLIENTS.stream()]

def new_client(username, email, password, image_code=False):
    """Creates a new client object in the database"""
    if username in list_clients(): return False
    CLIENTS.document(username).set({
        "username": username,
        "email": email,
        "password": password,
        "following": ["MilaFoods"],
        "saved": [],
        "image_code": image_code
    })
    return True

def update_client(username, data):
    """Updates a client object of the database"""
    CLIENTS.document(username).update(data)
    
def delete_client(username):
    """Deletes a client object of the database"""
    CLIENTS.document(username).delete()
    
def get_client(username):
    """Gets all the data of a client object of the database"""
    return CLIENTS.document(username).get().to_dict()
