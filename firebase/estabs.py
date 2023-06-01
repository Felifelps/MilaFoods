from .db import DB
import os
from .post import *
from .product import *
from .utils import encode_image, decode_image

ESTABS = DB.collection("estabs")

def list_estabs():
    return [i.id for i in ESTABS.stream()]

def new_estab(username, email, cpf, birth_date, cnpj, tel, password, description, image=None):
    """Creates a new estab object in the database"""
    if username in list_estabs(): return False
    new = ESTABS.document(username)
    new.set({
        "username": username,
        "email": email,
        "password": password,
        "cpf": cpf,
        "birth_date": birth_date,
        "cnpj": cnpj,
        "tel": tel,
        "description": description,
        "image": image if image == None else encode_image(image)
    })
    new.collection("menu")
    new.collection("posts")
    new_post(
        username,
        f"{username} acabou de criar sua conta!!",
        image
    )
    return True
    
def update_estab(username, data):
    """Updates a estab object of the database"""
    ESTABS.document(username).update(data)
    
def delete_estab(username):
    """Deletes a estab object of the database"""
    ESTABS.document(username).delete()
    
def get_estab(username):
    """Gets all the data of a client object of the database"""
    return ESTABS.document(username).get().to_dict()

def download_estab_image(username):
    estab = get_estab(username)
    path = os.path.join("data", username)
    if not os.path.exists(path): 
        os.mkdir(path)
    decode_image(estab["image"][1], "image." + estab["image"][0], path)
    
def change_estab_image(username, image_path):
    update_estab(username, {"image": encode_image(image_path)})
