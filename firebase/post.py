import datetime, os
from .db import DB
from .utils import encode_image, decode_image

async def new_post(id, username, text, image=""):
    key = f'{username}-{id}'
    if key in await list_posts(): return False
    await DB.document(f"posts/{key}").set({
        "id": id,
        "username": username,
        "text": text,
        "image": "image.png",
        "timestamp": str(datetime.datetime.today()).split(".")[0],
        "likes": 0,
        "comments": []
    })
    await upload_image(f'{username}-{id}', image)
    return True

async def update_post(key, data):
    await DB.document(f"posts/{key}").update(data)

async def get_post(key):
    post = await DB.document(f"posts/{key}").get()
    post = post.to_dict()
    post.update({'id': str(post['id'])})
    if post['image'] != '':
        await download_image(post)
    return post

async def download_image(post):
    if post['image'] == 'image.png': return post['image']
    post_key = f"{post['username']}-{post['id']}"
    image_path = os.path.join("data", "post_images", f"{post_key}.{post['image'][0]}")
    if not os.path.exists(image_path): 
        decode_image(post['image'][1], f"{post_key}.{post['image'][0]}")
    return image_path

async def upload_image(post, image_path):
    await update_post(post, {"image": image_path if image_path in 'image.png' else encode_image(image_path)})
        
async def list_posts(only_key=True, username=False):
    if not username:
        return [(post.id if only_key else post.to_dict()) async for post in DB.collection(f"posts").stream()]
    return [(post.id if only_key else post.to_dict()) async for post in DB.collection(f"posts").stream() if username in post.id]

async def delete_post(key):
    await DB.document(f"posts/{key}").delete()
    split = key.split('-')
    await DB.document(f"estabs/{split[0]}/posts/{split[1]}").delete()