import datetime
from db import DB
from utils import encode_image

def new_post(email, title, text, image=None):
    posts = DB.collection(f"estabs/{email}/posts")
    if title in [i.id for i in posts.stream()]:
        return "Already exists"
    timestamp = str(datetime.datetime.today()).split(".")[0]
    post = posts.document(timestamp) 
    post.set({
        "title": title,
        "text": text,
        "image": image if image == None else encode_image(image),
        "timestamp": timestamp
    })
    
def get_post(email, timestamp):
    for i in DB.collection(f"estabs/{email}/posts").stream():
        content = i.to_dict()
        if timestamp in content["timestamp"]:
            return content
        
def list_posts(email):
    return [i.id for i in DB.collection(f"estabs/{email}/posts").stream()]

def delete_post(email, timestamp):
    """Deletes a post object of the database"""
    content = get_post(email, timestamp)
    if content != None:
        DB.document(f"estabs/{email}/posts/{content['timestamp']}").delete()