from .db import DB, firestore
from .post import update_post, get_post

CLIENTS = DB.collection("clients")

def list_clients():
    return [i.id for i in CLIENTS.stream()]

def new_client(username, email, password, description, image_code=0):
    """Creates a new client object in the database"""
    if username in list_clients(): return False
    CLIENTS.document(username).set({
        "username": username,
        "email": email,
        "password": password,
        "following": ["MilaFoods"],
        "description": description,
        "saved": [],
        "liked": [],
        "image_code": image_code
    })
    return get_client(username)    

def client_like(username, post_id):
    update_post(post_id, {'likes': firestore.Increment(1)})
    update_client(username, {'liked': firestore.ArrayUnion([post_id])})

def client_un_like(username, post_id):
    update_post(post_id, {'likes': firestore.Increment(-1)})
    update_client(username, {'liked': firestore.ArrayRemove([post_id])})

def client_comment(username, post_id, comment_code):
    update_post(post_id, {'comments': firestore.ArrayUnion([f'{username}-{comment_code}'])})

def client_save(username, post_id):
    update_client(username, {'saved': firestore.ArrayUnion([post_id])})

def client_un_save(username, post_id):
    update_client(username, {'saved': firestore.ArrayRemove([post_id])})
    
def update_client(username, data):
    """Updates a client object of the database"""
    CLIENTS.document(username).update(data)
    
def save_post(username, timestamp, estab_username):
    update_client(username, {
        'saved': [f'{timestamp}-{estab_username}']
    })
    
def delete_client(username):
    """Deletes a client object of the database"""
    CLIENTS.document(username).delete()
    
def get_client(username):
    """Gets all the data of a client object of the database"""
    if username not in list_clients():
        return False
    return CLIENTS.document(username).get().to_dict()
