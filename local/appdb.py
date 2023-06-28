import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()
saved_cols = ['image', 'text', 'likes', 'timestamp', 'key']

def save_username(username):
    cursor.execute(f'update user set username = "{username}"')
    conn.commit()

def get_username():
    cursor.execute(f'select * from user')
    return list(cursor.fetchall())[0][0]

def get_theme():
    cursor.execute(f'select * from user')
    return list(cursor.fetchall())[0][1]

def alter_theme(theme):
    cursor.execute(f'''update user set theme = "{theme}" where rowid = 1;''')
    conn.commit()

def back_to_default_user():
    cursor.execute(f'update user set username = "===NoUser==="')
    conn.commit()

def local_save_post(post):
    cursor.execute(f'''insert into saved values (
       '{post['image']}',
       '{post['text']}',
       {post['likes']},
       '{post['timestamp']}',
       '{post['username']}-{post['id']}'
    );           
    ''')
    conn.commit()
    
def local_un_save_post(post_key):
    cursor.execute(f'''delete from saved where key = '{post_key}';''')
    conn.commit()

def get_local_saved_posts():
    posts = {}
    cursor.execute(f'select * from saved')
    for line in cursor.fetchall():
        post = {saved_cols[n] : line[n] for n in range(5)}
        posts[f'{line[4]}'] = post
    return posts

def erase_saved_data():
    cursor.execute('delete from saved;')
    print(get_local_saved_posts())
    conn.commit()

