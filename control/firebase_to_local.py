from firebase.client import new_client, get_client, delete_client
from local.appdb import *

def sign_up_and_login_new_client(username, email, password):
    new_client(username, email, password)
    
    
    