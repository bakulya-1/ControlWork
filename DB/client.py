
import sqlite3
from venv import create

connect = sqlite3.connect('clients.db')
cursor = connect.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS clients(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR (100) NOT NULL,
    age INTEGER NOT NULL,
    hobby TEXT
    )
""")
connect.commit()

def add_client(name, age, hobby = ""):
    cursor.execute('INSERT INTO clients(name, age, hobby) VALUES (?, ?, ?)', (name, age, hobby))
    connect.commit()
    print(f"Пользователь {name} добавлен.")

add_client('Izumi', 20, 'читать')
add_client('Kimiko', 23, 'Велосипед')
add_client('Momo', 20, 'волейбол')
add_client('Akaio', 24, 'плавать')
add_client('Djiro', 24, 'карате')

def get_all_clients():
    cursor.execute("SELECT * FROM clients")
    clients = cursor.fetchall()

    if clients:
        print(f"Список всех пользователей:")
        for client in clients:
            print(f"ID: {client[0]}, Name: {client[1]}, Age: {client[2]}, Hobby: {client[3]}")
    else:
        print(f"Список пользователей пуст")

    return clients
get_all_clients()

def update_client_name(client_id, name):
    cursor.execute("UPDATE clients SET name = ? WHERE id = ?", (name, client_id))
    connect.commit()
    print(f"Имя пользователя с ID {client_id} обновлено.")

update_client_name(3, 'Masako')

def delete_client(client_id):
    cursor.execute("DELETE FROM clients WHERE id = ?", (client_id,))
    connect.commit()

delete_client(4)

connect.close()








