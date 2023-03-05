from db import DB
import os, datetime
from post import *
from utils import encode_image, decode_image

ESTABS = DB.collection("estabs")

def list_estabs():
    return [i.id for i in ESTABS.stream()]

def new_estab(name, email, password, contact, description, image=None):
    """Creates a new estab object in the database"""
    new = ESTABS.document(email)
    new.set({
        "name": name,
        "email": email,
        "password": password,
        "contact": contact,
        "description": description,
        "image": image if image == None else encode_image(image)
    })
    new.collection("menu")
    new.collection("posts")
    new_post(
        email,
        "Bem-vindo ao app",
        name + " acabou de criar sua conta!!",
        image
    )
    
def update_estab(email, data):
    """Updates a estab object of the database"""
    ESTABS.document(email).update(data)
    
def delete_estab(email):
    """Deletes a estab object of the database"""
    ESTABS.document(email).delete()
    
def get_estab(email):
    """Gets all the data of a client object of the database"""
    return ESTABS.document(email).get().to_dict()

def download_estab_image(email):
    estab = get_estab(email)
    path = os.path.join("data", email)
    if not os.path.exists(path): 
        os.mkdir(path)
    decode_image(estab["image"][1], "image." + estab["image"][0], path)
    
def change_estab_image(email, image_path):
    update_estab(email, {"image": encode_image(image_path)})

