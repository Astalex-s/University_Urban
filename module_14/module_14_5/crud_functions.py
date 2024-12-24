import sqlite3


def initiate_db():
    connection = sqlite3.connect('product.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    price INTEGER NOT NULL
    );
    ''')
    # ДОБАВЛЕНИЕ ПРОДУКТОВ В ТАБЛИЦУ:
    # for i in range(1, 5):
    #     cursor.execute("INSERT INTO Products(title, description, price) VALUES (?, ?, ?)",
    #                    (f"Продукт {i}", f"Описание {i}", f"{i * 100}"))

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER NOT NULL,
        balance INTEGER NOT NULL
        );
        ''')

    connection.commit()
    connection.close()


# ДЕЛАЕМ ВЫБОРКУ ВСЕХ ЗАПИСЕЙ:
def get_all_products():
    connection = sqlite3.connect('product.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products")
    connection.commit()
    return cursor.fetchall()


def add_user(username, email, age):
    connection = sqlite3.connect('product.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (username, email, age, 1000))
    connection.commit()


def is_included(username):
    connection = sqlite3.connect('product.db')
    cursor = connection.cursor()
    user = cursor.execute("SELECT NOT EXISTS(SELECT username FROM Users WHERE username = ?)",
                          (username,)).fetchone()[0]
    connection.close()
    return bool(user)


if __name__ == "__main__":
    initiate_db()
