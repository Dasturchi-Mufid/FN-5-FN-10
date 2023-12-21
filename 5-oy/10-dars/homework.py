# 1) User deb nomlangan Database Table yarating unga username, password, f_name, age degan ustunlar qo`shing. 
# 2) userning ma`lumotlarini filterlash uchun funksiay yozing, u 3ta parameterni qabul qilsin 1-ustun nomi, 2-qiymati, 3-belgisi ('username', 'no_name', '==') 
# 3) ushbu funksiyani teng 3-4threadda ishga tushuring har safar funksiyaga boshqa parametrelar bering

import psycopg2
import threading

conn = psycopg2.connect(
    host="localhost",
    database="user",
    user="postgres",
    password="1"
)
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(255),
        password VARCHAR(255),
        f_name VARCHAR(255),
        age INTEGER
    )
''')
conn.commit()

def add_user(username, password, f_name, age):
    cursor.execute('INSERT INTO users (username, password, f_name, age) VALUES (%s, %s, %s, %s)', (username, password, f_name, age))
    conn.commit()

def filter_users(column_name, value, operator):
    query = f'SELECT * FROM users WHERE {column_name} {operator} %s'
    cursor.execute(query, (value,))
    result = cursor.fetchall()
    return result

user_data = [
    {'username': 'user1', 'f_name': 'John', 'age': 30},
    {'username': 'user2', 'f_name': 'Jane', 'age': 16},
]

for user in user_data:
    add_user(user['username'], 'password', user['f_name'], user['age'])

threads = []

filter_criteria = [
    ('username', 'user1', '='),
    ('f_name', 'Jane', '='),
    ('age', 25, '>=')
]

for column, value, operator in filter_criteria:
    thread = threading.Thread(target=filter_users, args=(column, value, operator))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

for column, value, operator in filter_criteria:
    result = filter_users(column, value, operator)
    print(f"Results for {column} {operator} {value}:")
    print(result)

conn.close()
