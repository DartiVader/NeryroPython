import sqlite3


connection = sqlite3.connect('db_dlya_nero.db')
cursor = connection.cursor()

def find_worker(sr_spec):
    cursor.execute(f"SELECT * FROM users WHERE Strength = {sr_spec[0]} AND Endurance = {sr_spec[1]} AND Intelligence = {sr_spec[2]} AND Charisma = {sr_spec[3]}")
    x = cursor.fetchone()
    if x is None:
        pass
        connection.commit()
    else:
        
        print(x)
    connection.commit()