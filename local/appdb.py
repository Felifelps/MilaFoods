import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

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
    

