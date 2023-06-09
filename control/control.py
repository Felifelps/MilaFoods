from firebase.user import new_client_user, new_estab_user, get_user, list_users, delete_user, update_user, user_like, user_save, user_comment, user_un_like
from firebase.post import new_post, get_post, list_posts
from local.appdb import *
from firebase.gmail import AuthenticationMail
import random

USER = get_user(get_user_data()['username'])

def send_email_code(email):
    for i in range(5):
        try:
            return AuthenticationMail.send_code_email(email)
        except Exception as e:
            print(e)
    return False

def send_validate_cpf_or_cnpj_email(cnpj, cpf, birth_date):
    for i in range(5):
        try:
            AuthenticationMail.send_cpf_or_cnpj_email(cnpj, cpf, birth_date)
            return True
        except Exception as e:
            print(e)
    return False

def check_if_a_account_was_validated(cpf_or_cnpj):
    for i in range(5):
        try:
            return AuthenticationMail.check_cpf_or_cnpj_confirmation(cpf_or_cnpj)
        except Exception as e:
            print(e)
    return False

def login_client(username, password):
    if username == '' or password == '':
        return 'Os campos devem ser preenchidos'
    if len(username) < 6:
        return 'O username deve conter 6 ou mais caracteres'
    for i in '''@#$%¨*()!"'.?/:;}]{[º^~´`\\|°=+-<>''':
        if i in username:
            return 'Caracteres inválidos para username'
    if len(password) < 6:
        return 'A senha deve conter 6 ou mais caracteres'
    user = get_user(username)
    if not user: return 'Crendenciais inválidas'
    if user['password'] == password:
        save_user_data(user)
    return user

def check_client_sign_up_inputs(username, email, password):
    if username == '' or email == '' or password == '':
        return 'Os campos devem ser preenchidos'
    if len(username) < 6:
        return 'O username deve conter 6 ou mais caracteres'
    for i in '''@#$%¨*()!"'.?/:;}]{[º^~´`\\|°=+-<>''':
        if i in username:
            return 'Caracteres inválidos para username'
    if username in list_users():
        return 'Username em uso'
    if '@' not in email or '.' not in email:
        return 'Email inválido'
    if len(password) < 6:
        return 'A senha deve conter 6 ou mais caracteres'
    return True

def sign_up_and_login_client(username, email, password):
    user = new_client_user(username, email, password, 'Sou novo no app!')
    if not user: return False
    save_user_data(user)
    return user

def login_estab(cpf_or_cnpj, password):
    users = list_users(True)
    for user in users:
        if user['can_post'] and (user['cpf'] == cpf_or_cnpj or user['cnpj'] == cpf_or_cnpj) and user['password'] == password:
            if not user['validated']:
                validated = check_if_a_account_was_validated(cpf_or_cnpj)
                if validated == None:
                    return 'Conta em validação.'
                elif validated == False:
                    delete_user(user['username'])
                    return 'Seus dados não são válidos. Tente recriar a conta.'
                elif validated:
                    update_user(user['username'], {'validated': True})
            save_user_data(get_user(user['username']))
            return True
    return 'Usuário não encontrado'
    
def check_estab_sign_up_inputs(username, email, password, cnpj, cpf, birth_date):
    if username == '' or email == '' or password == '' or (cnpj != None and len(cnpj) < 14 and cpf == None) or (cpf != None and len(cpf) < 11 and cnpj == None) or (cpf != None and 'Selecione' in birth_date):
        return 'Todos os campos devem ser preenchidos'
    if '@' not in email or '.' not in email:
        return 'Email inválido'
    if len(password) < 6:
        return 'A senha deve conter 6 ou mais caracteres'
    if len(username) < 6:
        return 'O username deve conter 6 ou mais caracteres'
    for i in '''@#$%¨*()!"'.?/:;}]{[º^~´`\\|°=+-<>''':
        if i in username:
            return 'Caracteres inválidos para username'
    key = cnpj if cpf == None else cpf
    users = list_users(True)
    for user in users:
        if username == user['username']:
            return 'Username em uso'
        if key == cnpj and user['cnpj'] == key:
            return 'CNPJ já cadastrado'
        if key == cpf and user['cpf'] == key:
            return 'CPF já cadastrado'
    return True
    
def sign_up_estab(username, email, password, cnpj, cpf, birth_date):
    user = new_estab_user(username, email, cpf, birth_date, cnpj, None, password, 'Sou novo no app!', None)
    return user

def get_posts_from_server(randomize=True):
    posts = list_posts(False)
    user = get_user(USER['username'])
    save_user_data(user)
    for post in posts:
        post['id'] = str(post['id'])
        post['height'] = 300
        post['liked'] = f"{post['username']}-{post['id']}" in user['liked']
    if randomize: random.shuffle(posts)
    return posts 
        
def get_local_user_data():
    return get_user_data()

def logout():
    back_to_default_user()

def save_theme(theme):
    alter_theme(theme)