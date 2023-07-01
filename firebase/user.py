from .db import DB, firestore_async, os
from .post import list_posts, new_post, get_post, update_post
from .utils import encode_image, decode_image, user_image_was_loaded
try:
    USERS = DB.collection("users")
except Exception as e:
    input(e)

async def list_users(all=False):
    users = []
    if all:
        async for i in USERS.stream():
            users.append(i.to_dict())
    else:
        async for i in USERS.stream():
            users.append(i.id)
    return users

async def get_user(username):
    if username not in await list_users():
        return False
    user = await USERS.document(username).get()
    user = user.to_dict()
    if user['can_post'] and user['image'] != '':
        await download_image(user)
        user.update({'image': f'{user["username"]}.{user["image"][0]}'})
    else:
        user.update({'image': 'account-circle.png'})
    print(user)
    return user

async def new_client_user(username, email, password, description):
    if username in await list_users(): return False
    await USERS.document(username).set({
        "username": username,
        "email": email,
        "password": password,
        "cpf": None,
        "birth_date": None,
        "cnpj": None,
        "tel": None,
        "description": description,
        "image": "",
        "image_code": 0,
        "n_of_posts": None,
        "liked": [],
        "saved": [],
        "following": ['MilaFoods'],
        "n_of_followers": None,
        "can_post": False,
        "validated": True
    })
    await list_users()
    return await get_user(username)   

async def new_estab_user(username, email, cpf, birth_date, cnpj, tel, password, description):
    if username in await list_users(): return False
    user = USERS.document(username)
    await user.set({
        "username": username,
        "email": email,
        "password": password,
        "cpf": cpf,
        "birth_date": birth_date,
        "cnpj": cnpj,
        "tel": tel,
        "description": description,
        "image": "",
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
    await new_post(
        1,
        username,
        f"Acabei de criar minha conta!!"
    )
    await list_users()
    return await get_user(username)

async def get_user_posts(username):
    posts = []
    async for i in DB.collection(f"users/{username}/posts").stream():
        posts.append(i.to_dict())
    return posts

async def user_like(username, post_id):
    await update_post(post_id, {'likes': firestore_async.Increment(1)})
    await update_user(username, {'liked': firestore_async.ArrayUnion([post_id])})

async def user_un_like(username, post_id):
    await update_post(post_id, {'likes': firestore_async.Increment(-1)})
    await update_user(username, {'liked': firestore_async.ArrayRemove([post_id])})

async def user_follow(username, following_username):
    await update_user(username, {'following': firestore_async.ArrayUnion([following_username])})
    await update_user(following_username, {'n_of_followers': firestore_async.Increment(1)})

async def user_un_follow(username, following_username):
    await update_user(username, {'following': firestore_async.ArrayRemove([following_username])})
    await update_user(following_username, {'n_of_followers': firestore_async.Increment(-1)})

async def user_comment(username, post_id, comment_code):
    await update_post(post_id, {'comments': firestore_async.ArrayUnion([f'{username}-{comment_code}'])})

async def user_save(username, post_id):
    await update_user(username, {'saved': firestore_async.ArrayUnion([post_id])})

async def user_un_save(username, post_id):
    await update_user(username, {'saved': firestore_async.ArrayRemove([post_id])})
    
async def post(username, text, image):
    user = await get_user(username)
    if not user['can_post']: return False
    id = user['n_of_posts'] + 1
    await new_post(id, username, text, image)
    print(f'Posted {username}-{id}')
    await update_user(username, {"n_of_posts": id})
    
async def update_user(username, data):
    """Updates a client object of the database"""
    await USERS.document(username).update(data)
    
async def save_post(username, timestamp, estab_username):
    await update_user(username, {
        'saved': [f'{timestamp}-{estab_username}']
    })
    
async def delete_user(username):
    """Deletes a client object of the database"""
    await USERS.document(username).delete()
    await list_users()

async def download_image(user):
    if user['image'] == '':
        return os.path.join("views", "data", "user_images", f"account-circle.png")
    for i in os.listdir(os.path.join('views', 'data', 'user_images')):
        if user['username'] in i:
            os.remove(os.path.join('views', 'data', 'user_images', i))
            break
    decode_image(user['image'][1], f"{user['username']}.{user['image'][0]}")
    return os.path.join("views", "data", "user_images", f"{user['username']}.{user['image'][0]}")
    
async def upload_image(username, image_path):
    await update_user(username, {"image": '' if image_path == '' else encode_image(image_path)})