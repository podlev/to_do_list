import sqlite3

con = sqlite3.connect('to_do_list.sqlite')
cur = con.cursor()


def check_bd():
    cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL,
                name VARCHAR(255)
                );
                """)
    cur.execute("""
                CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                title VARCHAR(255) NOT NULL,
                descriptions VARCHAR(255),
                deadline_date DATETIME,
                FOREIGN KEY (user_id) REFERENCES users (id)
                );
                """)
    con.commit()

def add_user(username, password, name):
    cur.execute("""
                INSERT INTO users (username, password, name)
                VALUES (?, ?, ?)""", (username, password, name))
    con.commit()

def login(username, password) -> bool:
    result = cur.execute("""
                         SELECT username, password, name
                         FROM users
                         WHERE username = (?)""", (username,)).fetchone()
    if result is None:
        print('Нет такого пользователя.')
        return False
    elif result[1] != password:
        print('Неверный пароль.')
        return False
    print(f'Добро пожаловать, {result[2]}!')
    return True

check_bd()
# add_user('user', '123456', 'Лев')
login('user', '123456')