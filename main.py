import sqlite3

con = sqlite3.connect('to_do_list.sqlite')
cur = con.cursor()


def check_bd():
    cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                id INT PRIMARY KEY,
                username VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL,
                name VARCHAR(255)
                );
                """)
    cur.execute("""
                CREATE TABLE IF NOT EXISTS tasks (
                id INT PRIMARY KEY,
                user_id INT,
                title VARCHAR(255) NOT NULL,
                descriptions VARCHAR(255),
                deadline_date DATETIME,
                FOREIGN KEY (user_id) REFERENCES users (id)
                );
                """)
    con.commit()


check_bd()