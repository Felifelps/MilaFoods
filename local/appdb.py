import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

def save_client_data(username, email, password, theme, image_code=None, following=[], saved=[]):
    cursor.execute(f'''
update user 
set username = "{username}",   
    email = "{email}",
    theme = "{theme}",
where rowid = 1;         
    ''')
    conn.commit()

def saved_estab_data(username, email, password, description, cpf=None, birth_date=None, cnpj=None, tel=None, image=None)
    
def get_user_data():
    cursor.execute('select * from user')
    return list(cursor.fetchall())[0]
