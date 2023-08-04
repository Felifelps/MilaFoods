from firebase.user import *
from firebase.post import *
from local.appdb import *
from firebase.gmail import AuthenticationMail
import random, os

Email = None
POSTS = []

async def send_email_code(email):
    if Email == None: Email = AuthenticationMail()
    for i in range(30): #300 seconds tiemout
        try:
            return await Email.send_code_email(email)
        except Exception as e: 
            print(e)
    return False

async def send_validate_cpf_or_cnpj_email(cnpj, cpf, birth_date):
    if Email == None: Email = AuthenticationMail()
    for i in range(30): #300 seconds tiemout
        try:
            await Email.send_cpf_or_cnpj_email(cnpj, cpf, birth_date)
            return True
        except Exception as e:
            print(e)
    return False

async def check_if_a_account_was_validated(cpf_or_cnpj):
    if Email == None: Email = AuthenticationMail()
    for i in range(30): #300 seconds tiemout
        try:
            return await Email.check_cpf_or_cnpj_confirmation(cpf_or_cnpj)
        except Exception as e:
            print(e)
    return False

async def login_client(username, password):
    if username == '' or password == '':
        return 'Os campos devem ser preenchidos'
    if len(username) < 6:
        return 'O username deve conter 6 ou mais caracteres'
    for i in '''@#$%¨*()!"'?/:;}]{[º^~´`\\|°=+-<>''':
        if i in username:
            return 'Caracteres inválidos para username'
    if len(password) < 6:
        return 'A senha deve conter 6 ou mais caracteres'
    user = await get_user(username)
    if not user: return 'Crendenciais inválidas'
    if user['password'] == password:
        save_username(username)
        await server_saved_to_local(username)
    return f'Logged:{username}'

async def check_client_sign_up_inputs(username, email, password):
    if username == '' or email == '' or password == '':
        return 'Os campos devem ser preenchidos'
    if len(username) < 6:
        return 'O username deve conter 6 ou mais caracteres'
    for i in '''@#$%¨*()!"'.?/:;}]{[º^~´`\\|°=+-<>''':
        if i in username:
            return 'Caracteres inválidos para username'
    if username in await list_users():
        return 'Username em uso'
    if '@' not in email or '.' not in email:
        return 'Email inválido'
    if len(password) < 6:
        return 'A senha deve conter 6 ou mais caracteres'
    return True

async def sign_up_and_login_client(username, email, password):
    user = await new_client_user(username, email, password, '')
    if not user: return False
    save_username(username)
    server_saved_to_local(user['username'])
    return user

async def login_estab(cpf_or_cnpj, password):
    users = await list_users(True)
    for user in users:
        if user['can_post'] and (user['cpf'] == cpf_or_cnpj or user['cnpj'] == cpf_or_cnpj) and user['password'] == password:
            if not user['validated']:
                validated = await check_if_a_account_was_validated(cpf_or_cnpj)
                if validated == None:
                    return 'Conta em validação.'
                elif validated == False:
                    await delete_user(user['username'])
                    return 'Seus dados não são válidos. Tente recriar a conta.'
                elif validated:
                    await update_user(user['username'], {'validated': True})
            save_username(user['username'])
            await server_saved_to_local(user['username'])
            return user
    return 'Usuário não encontrado'

async def check_estab_sign_up_inputs(username, email, password, cnpj, cpf, birth_date):
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
    users = await list_users(True)
    for user in users:
        if username == user['username']:
            return 'Username em uso'
        if key == cnpj and user['cnpj'] == key:
            return 'CNPJ já cadastrado'
        if key == cpf and user['cpf'] == key:
            return 'CPF já cadastrado'
    return True
    
async def sign_up_estab(username, email, password, cnpj, cpf, birth_date):
    return await new_estab_user(username, email, cpf, birth_date, cnpj, None, password, '')

async def server_saved_to_local(username):
    user = await get_user(username)
    erase_saved_data()
    for saved in user['saved']:
        local_save_post(await get_post(saved))

async def get_posts_from_server():
    global POSTS
    if POSTS == []:
        POSTS = [await get_post(i) for i in await list_posts()]
    POSTS = await update_posts(POSTS)
    return random.sample(POSTS, 25 if len(POSTS) >= 25 else len(POSTS))

async def update_posts(posts):
    user = await get_user(get_username())
    for post in posts:
        post.update({
            'id': str(post['id']),
            'height': 300,
            'liked': f"{post['username']}-{post['id']}" in user['liked'],
            'saved': f"{post['username']}-{post['id']}" in user['saved'],
            'user_image': user_image_was_loaded(post['username'])
        })
    return posts

def logout():
    back_to_default_user()

def save_theme(theme):
    alter_theme(theme)

async def save_post(post_id):
    await user_save(get_username(), post_id)
    local_save_post(await get_post(post_id))

async def un_save_post(post_id):
    await user_un_save(get_username(), post_id)
    local_un_save_post(post_id)
    