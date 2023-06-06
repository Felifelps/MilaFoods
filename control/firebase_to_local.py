from firebase.client import new_client, get_client, list_clients, client_like, client_comment, client_un_like
from firebase.estabs import new_estab, get_estab, post, get_post, list_posts, estab_like, estab_comment, estab_un_like
from local.appdb import *

def send_email_code(email):
    for i in range(5):
        try:
            from firebase.authenticate_email import send_code_email
            return send_code_email(email)
        except Exception as e:
            print(e)
    return False

def check_username_and_password(username, password):
    if username == '' or password == '':
        return 'Os campos devem ser preenchidos'
    if len(username) < 6:
        return 'O username deve conter 6 ou mais caracteres'
    for i in '''@#$%¨*()!"'.?/:;}]{[º^~´`\\|°=+-<>''':
        if i in username:
            return 'Caracteres inválidos para username'
    if len(password) < 6:
        return 'A senha deve conter 6 ou mais caracteres'
    client = login_client(username, password)
    if not client:
        return 'Credenciais inválidas'
    return client

def check_username_email_and_password(username, email, password):
    if username == '' or email == '' or password == '':
        return 'Os campos devem ser preenchidos'
    if len(username) < 6:
        return 'O username deve conter 6 ou mais caracteres'
    for i in '''@#$%¨*()!"'.?/:;}]{[º^~´`\\|°=+-<>''':
        if i in username:
            return 'Caracteres inválidos para username'
    if username in list_clients():
        return 'Username em uso'
    if '@' not in email or '.' not in email:
        return 'Email inválido'
    if len(password) < 6:
        return 'A senha deve conter 6 ou mais caracteres'
    return True

def login_client(username, password):
    client = get_client(username)
    if not client: return False
    if client['password'] == password:
        save_client_data(
            username,
            client['email'],
            client['password'],
            'Red',
            client['description'],
            client['image_code'],
            client['following'],
            client['saved']
        )
        return client
    
def sign_up_and_login_new_client(username, email, password):
    client = new_client(username, email, password, 'Sou novo no app!')
    if not client:
        return False
    save_client_data(username, client['email'], client['password'], 'Red', 'Sou novo no app!', client['image_code'], client['following'], client['saved'])
    return get_client(username)

def update_posts():
    posts = []
    local_posts = [f'{i["username"]}-{i["id"]}' for i in get_posts_data()]
    for post in list_posts():
        if post not in local_posts:
            print('Loading', post)
            posts.append(get_post(post))
    save_posts_data(posts)
    
def get_posts_from_db():
    return get_posts_data()
        
def get_local_user_data():
    return get_user_data()

def logout():
    back_to_default_user()

def save_theme(theme):
    alter_theme(theme)