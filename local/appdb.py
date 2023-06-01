import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

def save_user_data(username, email, theme, type):
    cursor.execute(f'''
update user 
set username = "{username}",   
    email = "{email}",
    theme = "{theme}",
    type = "{type}"
where rowid = 1;         
    ''')
    conn.commit()
    
def get_user_data():
    cursor.execute('select * from user')
    return list(cursor.fetchall())[0]
