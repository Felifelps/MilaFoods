import datetime, os
from .db import DB
from .utils import encode_image, decode_image

def new_post(id, username, text, image=""):
    key = f'{username}-{id}'
    if key in list_posts(): return False
    DB.document(f"posts/{key}").set({
        "id": id,
        "username": username,
        "text": text,
        "image": image if image == "" else encode_image(image),
        "timestamp": str(datetime.datetime.today()).split(".")[0],
        "likes": 0,
        "comments": []
    })
    DB.document(f"users/{username}/posts/{key}").set({"id": id})
    return True

def update_post(key, data):
    DB.document(f"posts/{key}").update(data)

def get_post(key):
    post = DB.document(f"posts/{key}").get().to_dict()
    if post['image'] != '':
        download_image(post)
    return post

def download_image(post):
    post_key = f"{post['username']}-{post['id']}"
    image_path = os.path.join("data", "post_images", f"{post_key}.{post['image'][0]}")
    if not os.path.exists(image_path): 
        decode_image(post['image'][1], f"{post_key}.{post['image'][0]}")
    return image_path
        
def list_posts(only_key=True, username=False):
    if not username:
        return [(post.id if only_key else post.to_dict())for post in DB.collection(f"posts").stream()]
    return [(post.id if only_key else post.to_dict()) for post in DB.collection(f"posts").stream() if username in post.id]

def delete_post(key):
    DB.document(f"posts/{key}").delete()
    split = key.split('-')
    DB.document(f"estabs/{split[0]}/posts/{split[1]}").delete()