import sqlite3
connection = sqlite3.connect(r"D:\University_Urban\module_14\module_14_1\not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')
# ЗАПОЛНЯЕМ БАЗУ ДАННЫХ 10-Ю НОВЫМИ ЗАПИСЯМИ:
# for i in range(1, 11):
#     cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES (?, ?, ?, ?)",
#                    (f"User{i}", f"example{i}@gmail.com", f"{i * 10}", 1000))

# ОБНОВЛЯЕМ balance У КАЖДОЙ 2-ОЙ ЗАПИСИ НАЧИНАЯ С 1-ОЙ НА 500:
# for i in range(1, 11, 2):
#     cursor.execute("UPDATE Users SET balance = ? WHERE id = ?", (500, i))

# УДАЛЯЕМ КАЖДУЮ 3-Ю ЗАПИСЬ В ТАБЛИЦК НАЧИНАЯ С 1-Й:
# for i in range(1, 11, 3):
#     cursor.execute("DELETE FROM Users WHERE id = ?", (i,))

# ДЕЛАЕМ ВЫБОРКУ ВСЕХ ЗАПИСЕЙ, КРОМЕ ЗАПИСИ ГДЕ ВОЗРАСТ РАВЕН 60:
# cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != ?", (60,))
# users = cursor.fetchall()
# for user in users:
#     print(f"Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}")

# УДАЛЯЕМ ПОЛЬЗОВАТЕЛЯ С ID=6:
# cursor.execute("DELETE FROM Users WHERE id = ?", (6,))

# ПОДСЧИТЫВАЕМ КОЛИЧЕСТВО ВСЕХ ПОЛЬЗОВАТЕЛЕЙ:
cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]

# ПОДСЧИТЫВАЕМ СУММУ ВСЕХ БАЛАНСОВ ПОЛЬЗОВАТЕЛЕЙ:
cursor.execute("SELECT SUM(balance) FROM Users")
all_balances = cursor.fetchone()[0]

# ВЫВОДИМ В КОНСОЛЬ СРЕДНИЙ БАЛАНС ВСЕХ ПОЛЬЗОВАТЕЛЕЙ
print(all_balances / total_users)

connection.commit()
connection.close()
