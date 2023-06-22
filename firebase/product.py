from .db import DB
from .utils import encode_image

async def list_products(username):
    return await [i.id for i in DB.collection(f"users/{username}/menu").stream()]

async def new_product(username, name, description, price, category_id, image=None):
    #['bebidas', 'doces', 'salgados', 'lanches', 'pratos'][category_id]
    if name in await list_products(username): return False
    product = await DB.collection(f"users/{username}/menu").document(name) 
    await product.set({
        "name": name,
        "description": description,
        "image": image if image == None else encode_image(image),
        "price": price,
        "category_id": category_id
    })
    return True

async def update_product(username, name, data):
    await DB.collection(f"users/{username}/menu").document(name).update(data)

async def get_product(username, name):
    for i in await DB.collection(f"users/{username}/menu").stream():
        content = i.to_dict()
        if name in content["name"]:
            return content

async def delete_product(username, name):
    """Deletes a product object of the database"""
    content = await get_product(username, name)
    if content != None:
        await DB.document(f"users/{username}/menu/{content['name']}").delete()
