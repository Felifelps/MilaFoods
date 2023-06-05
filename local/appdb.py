import sqlite3, random

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

def save_client_data(username, email, password, theme, description, image_code=None, following=[], saved=[]):
    cursor.execute(f'''
update user 
set username = "{username}",
    email = "{email}", 
    theme = "{theme}",
    password = "{password}",
    image_code = "{image_code}", 
    description = "{description}",   
    cpf = null,   
    birth_date = null,  
    cnpj = null,   
    tel = null,   
    image = null
where rowid = 1;         
    ''')
    cursor.execute('delete from "following";')
    for username in following:
        cursor.execute(f'insert into following values ("{username}");')
    conn.commit()

def save_estab_data(username, email, password, theme, description, cpf=None, birth_date=None, cnpj=None, tel=None, image=None):
    cursor.execute(f'''
update user 
set username = "{username}",   
    email = "{email}",   
    theme = "{theme}", 
    password = "{password}",  
    image_code = null,
    description = "{description}",   
    cpf = "{cpf}",   
    birth_date = "{birth_date}", 
    cnpj = "{cnpj}",   
    tel = "{tel}",   
    image = "{image}"
where rowid = 1;         
    ''')
    conn.commit()

def get_user_data():
    cursor.execute(f'select * from user')
    columns = list(map(lambda x: x[0], cursor.description))
    data = list(cursor.fetchall())[0]
    return {columns[x]: (data[x].replace("'", "") if isinstance(data[x], str) else data[x]) for x in range(len(columns))}

def back_to_default_user():
    cursor.execute('''
update user 
set username = "===++UserDefault++==="
where rowid = 1;         
    ''')
    conn.commit()
    
def alter_theme(theme):
    cursor.execute(f'''
update user 
set theme = "{theme}"
where rowid = 1;         
    ''')
    conn.commit()
    
def save_posts_data(posts):
    if posts == []: return 
    for post in posts:
        cursor.execute(f'''insert into posts values ("{post['username']}",
        {post['id']},
        "{post['text']}",
        "{post["image"]}",
        {post['likes']},
        "{post['timestamp']}"
    )
''')
    conn.commit()
    
def get_posts_data():
    posts = []
    cursor.execute('select * from posts;')
    for line in cursor.fetchall():
        posts.append({
            'username': line[0],
            'id': str(line[1]),
            'text': line[2],
            'image': str(line[3]),
            'likes': line[4],
            'timestamp': line[5],
            'height': 300 #For the post class
        })
    return random.sample(posts, len(posts))