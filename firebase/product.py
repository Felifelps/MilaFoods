import datetime
from .db import DB
from .utils import encode_image

def list_products(username):
    return [i.id for i in DB.collection(f"estabs/{username}/menu").stream()]

def new_product(username, name, description, price, category_id, image=None):
    #['bebidas', 'doces', 'salgados', 'lanches', 'pratos'][category_id]
    products = DB.collection(f"estabs/{username}/menu")
    if name in list_products(username): return False
    product = products.document(name) 
    product.set({
        "name": name,
        "description": description,
        "image": image if image == None else encode_image(image),
        "price": price,
        "category_id": category_id
    })
    return True

def update_product(username, name, data):
    DB.collection(f"estabs/{username}/menu").document(name).update(data)

def get_product(username, name):
    for i in DB.collection(f"estabs/{username}/menu").stream():
        content = i.to_dict()
        if name in content["name"]:
            return content

def delete_product(username, name):
    """Deletes a product object of the database"""
    content = get_product(username, name)
    if content != None:
        DB.document(f"estabs/{username}/menu/{content['name']}").delete()
