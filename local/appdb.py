import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

def save_user_data(username, email, password, following):
    cursor.execute(f'insert into user values ("{username}", "{email}", "{password}", {following})')
    conn.commit()
    
def get_user_data():
    cursor.execute('select * from user')
    return list(cursor.fetchall())
