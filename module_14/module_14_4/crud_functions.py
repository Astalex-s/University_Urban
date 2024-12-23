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
    for i in range(1, 5):
        cursor.execute("INSERT INTO Products(title, description, price) VALUES (?, ?, ?)",
                       (f"Продукт {i}", f"Описание {i}", f"{i * 100}"))

    connection.commit()
    connection.close()


# ДЕЛАЕМ ВЫБОРКУ ВСЕХ ЗАПИСЕЙ:
def get_all_products():
    connection = sqlite3.connect('Product.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products")
    connection.commit()
    return cursor.fetchall()


if __name__ == "__main__":
    initiate_db()
