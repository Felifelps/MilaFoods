import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

def save_user_data(user_data):
    query = 'update user set'
    n = 0
    for field, value in user_data.items():
        if isinstance(value, list): continue
        query += f' {field} = '
        if value == None: query += 'null '
        elif isinstance(value, str): query += f'"{value}" '
        elif isinstance(value, bool): query += f'{1 if value else 0} '
        elif isinstance(value, int): query += f'{value} '
        query += '' if field == 'cpf' else ','
        n += 1
    cursor.execute(query + 'where rowid = 1;')
    conn.commit()
    
def save_saved_data(saved_data):
    for saved in saved_data:
        cursor.execute(f'''insert into saved (text, image, id, username, likes) values (
            "{saved['text']}",
            "{saved['username']}",
            {saved['id']},
            "{saved['timestamp']}",
            "{saved['username']}",
            {saved['likes']}
        );              
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
    

