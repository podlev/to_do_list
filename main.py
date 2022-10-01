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

check_bd()
add_user('user', '123456', 'Лев')