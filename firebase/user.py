import os
from .db import DB, firestore
from .post import update_post, new_post
from .utils import encode_image, decode_image

USERS = DB.collection("users")
ALL_USERS = [i.id for i in USERS.stream()]

def list_users(all=False):
    if all:
        return [i.to_dict() for i in USERS.stream()]
    global ALL_USERS
    ALL_USERS = [i.id for i in USERS.stream()]
    return ALL_USERS

def new_client_user(username, email, password, description, image_code=0):
    if username in ALL_USERS: return False
    user = USERS.document(username).set({
        "username": username,
        "email": email,
        "password": password,
        "cpf": None,
        "birth_date": None,
        "cnpj": None,
        "tel": None,
        "description": description,
        "image": None,
        "image_code": image_code,
        "n_of_posts": None,
        "liked": [],
        "saved": [],
        "following": ['MilaFoods'],
        "n_of_followers": None,
        "can_post": False,
        "validated": True
    })
    list_users()
    return user.get().to_dict()   

def new_estab_user(username, email, cpf, birth_date, cnpj, tel, password, description, image=None):
    if username in ALL_USERS: return False
    user = USERS.document(username)
    user.set({
        "username": username,
        "email": email,
        "password": password,
        "cpf": cpf,
        "birth_date": birth_date,
        "cnpj": cnpj,
        "tel": tel,
        "description": description,
        "image": image if image == None else encode_image(image),
        "image_code": None,
        "n_of_posts": 1,
        "liked": [],
        "saved": [],
        "following": ['MilaFoods'],
        "n_of_followers": 0,
        "can_post": True,
        "validated": False
    })
    user.collection("menu")
    user.collection("posts")
    new_post(
        1,
        username,
        f"{username} acabou de criar sua conta!!",
        image
    )
    list_users()
    return user.get().to_dict()

def user_like(username, post_id):
    update_post(post_id, {'likes': firestore.Increment(1)})
    update_user(username, {'liked': firestore.ArrayUnion([post_id])})

def user_un_like(username, post_id):
    update_post(post_id, {'likes': firestore.Increment(-1)})
    update_user(username, {'liked': firestore.ArrayRemove([post_id])})

def user_comment(username, post_id, comment_code):
    update_post(post_id, {'comments': firestore.ArrayUnion([f'{username}-{comment_code}'])})

def user_save(username, post_id):
    update_user(username, {'saved': firestore.ArrayUnion([post_id])})

def client_un_save(username, post_id):
    update_user(username, {'saved': firestore.ArrayRemove([post_id])})
    
def post(username, text, image):
    user = get_user(username)
    if not user['can_post']: return False
    id = user['n_of_posts'] + 1
    new_post(id, username, text, image)
    print(f'Posted {username}-{id}')
    update_user(username, {"n_of_posts": id})
    
def update_user(username, data):
    """Updates a client object of the database"""
    USERS.document(username).update(data)
    
def save_post(username, timestamp, estab_username):
    update_user(username, {
        'saved': [f'{timestamp}-{estab_username}']
    })
    
def delete_user(username):
    """Deletes a client object of the database"""
    USERS.document(username).delete()
    list_users()
    
def get_user(username):
    """Gets all the data of a client object of the database"""
    if username not in ALL_USERS:
        return False
    return USERS.document(username).get().to_dict()

def download_image(username):
    user = get_user(username)
    if not user['can_post']: return
    path = os.path.join("data", username)
    if not os.path.exists(path): 
        os.mkdir(path)
    decode_image(user["image"][1], "image." + user["image"][0], path)
    
def update_image(username, image_path):
    update_user(username, {"image": encode_image(image_path)})