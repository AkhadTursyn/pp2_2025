import psycopg2
import csv

conn = psycopg2.connect(
    host="localhost",
    database="phonebook",
    user="postgres",
    password="070714",
    port=5432
)
cur = conn.cursor()

def insert_from_csv(filename):
    with open(filename, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            cur.execute("INSERT INTO contacts (name, phone) VALUES (%s, %s)", (row[0], row[1]))
    conn.commit()

def insert_manual():
    name = input("Введите имя: ")
    phone = input("Введите телефон: ")
    cur.execute("INSERT INTO contacts (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()

def update_user():
    old_name = input("Введите имя для обновления: ")
    new_name = input("Новое имя: ")
    new_phone = input("Новый телефон: ")
    cur.execute("UPDATE contacts SET name=%s, phone=%s WHERE name=%s", (new_name, new_phone, old_name))
    conn.commit()

def search_user():
    name = input("Введите имя для поиска: ")
    cur.execute("SELECT * FROM contacts WHERE name=%s", (name,))
    print(cur.fetchall())

def delete_user():
    name = input("Введите имя для удаления: ")
    cur.execute("DELETE FROM contacts WHERE name=%s", (name,))
    conn.commit()

insert_manual()
# insert_from_csv("Lab10/phonebook/data.csv")
update_user()
search_user()
delete_user()

cur.close()
conn.close()