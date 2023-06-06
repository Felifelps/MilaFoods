import sqlite3, random

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

def save_client_data(username, email, password, theme, description, image_code=None, following=[], saved=[], liked=[]):
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
    cursor.execute('delete from "liked";')
    for username in liked:
        cursor.execute(f'insert into liked values ("{username}");')
    cursor.execute('delete from "following";')
    for username in following:
        cursor.execute(f'insert into following values ("{username}");')
    cursor.execute('delete from "saved";')
    for post in saved:
        cursor.execute(f'insert into saved values ("{post}");')
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

def get_following_data():
    cursor.execute(f'select * from following')
    return list(map(lambda x: x[0], cursor.fetchall()))

def get_liked_data():
    cursor.execute(f'select * from liked')
    return list(map(lambda x: x[0], cursor.fetchall()))

def get_saved_data():
    cursor.execute(f'select * from saved')
    return list(map(lambda x: x[0], cursor.fetchall()))

def add_following_data(following):
    cursor.execute(f'insert into following values ("{following}");')
    conn.commit()

def add_liked_data(liked):
    cursor.execute(f'insert into liked values ("{liked}");')
    conn.commit()

def add_saved_data(saved):
    cursor.execute(f'insert into saved values ("{saved}");')
    conn.commit()

def remove_following_data(following):
    cursor.execute(f'delete from following where username = "{following}";')
    conn.commit()

def remove_liked_data(liked):
    cursor.execute(f'delete from liked where post_id = "{liked}";')
    conn.commit()

def remove_saved_data(saved):
    cursor.execute(f'delete from saved where post_id = "{saved}";')
    conn.commit()

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
            'height': 300, 
            'liked': True if f'{line[0]}-{line[1]}' in get_liked_data() else False
        })
    return random.sample(posts, len(posts))