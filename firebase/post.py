import datetime
from .db import DB
from .utils import encode_image

def new_post(username, text, image=None):
    posts = DB.collection(f"estabs/{username}/posts")
    timestamp = str(datetime.datetime.today()).split(".")[0]
    post = posts.document(timestamp) 
    post.set({
        "text": text,
        "image": image if image == None else encode_image(image),
        "timestamp": timestamp,
        "likes": 0
    })
    return True

def update_post(username, timestamp, data):
    """Updates a client object of the database"""
    DB.collection(f"estabs/{username}/posts").document(timestamp).update(data)

def get_post(username, timestamp):
    for i in DB.collection(f"estabs/{username}/posts").stream():
        content = i.to_dict()
        if timestamp in content["timestamp"]:
            return content
        
def list_posts(username):
    return [i.id for i in DB.collection(f"estabs/{username}/posts").stream()]

def delete_post(username, timestamp):
    """Deletes a post object of the database"""
    content = get_post(username, timestamp)
    if content != None:
        DB.document(f"estabs/{username}/posts/{content['timestamp']}").delete()