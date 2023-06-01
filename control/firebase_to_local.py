from firebase.client import new_client, get_client, list_clients, delete_client
from firebase.estabs import new_estab, get_estab
from firebase.authenticate_email import send_code_email
from local.appdb import *

def login_client(username, password):
    client = get_client(username)
    if not client: return False
    if client['password'] == password:
        save_client_data(
            username,
            client['email'],
            client['password'],
            'Red',
            client['image_code'],
            client['following'],
            client['saved']
        )
        return client
    
def sign_up_and_login_new_client(username, email, password):
    client = new_client(username, email, password)
    if not client:
        return False
    save_client_data(username, client['email'], client['password'], 'Red', client['image_code'], client['following'], client['saved'])
    return get_client(username)

def get_local_user_data():
    return get_user_data()

def logout():
    back_to_default_user()

    
    
