from firebase.client import new_client, get_client, list_clients, delete_client
from firebase.estabs import new_estab, get_estab
from firebase.authenticate_email import send_code_email
from local.appdb import *

def login_client(username, password):
    client = get_client(username)
    if not client: return False
    if client['password'] == password:
        save_user_data(username, client['email'], 'Red', 'client')
        return client
    
def sign_up_and_login_new_client(username, email, password):
    if not new_client(username, email, password):
        return False
    save_user_data(username, email, 'Red', 'client')
    return get_client(username)

def get_local_user_data():
    return get_user_data()

    
    
