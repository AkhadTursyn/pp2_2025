import psycopg2
from tabulate import tabulate

conn=psycopg2.connect(
    host="localhost",
    dbname="suppliers",
    user="postgres",
    password="030307", 
    port=31860
)
cur=conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS phonebook(
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    surname VARCHAR(255) NOT NULL,
    phone VARCHAR(255) UNIQUE NOT NULL
)
""")
conn.commit()

def search_by_pattern():
    pattern=input("Enter pattern to search(part of name, surname or phone):")
    query="""
        SELECT * FROM phonebook
        WHERE name ILIKE %s OR surname ILIKE %s OR phone ILIKE %s
    """
    cur.execute(query, (f"%{pattern}%", f"%{pattern}%", f"%{pattern}%"))
    results=cur.fetchall()
    if results:
        print(tabulate(results, headers=["ID", "Name", "Surname", "Phone"], tablefmt='fancy_grid'))
    else:
        print("No matches found")

def insert_or_update_user():
    name=input("Enter name: ")
    phone=input("Enter phone: ")
    cur.execute("SELECT * FROM phonebook WHERE name=%s", (name,))
    if cur.fetchall():
        cur.execute("UPDATE phonebook SET phone=%s WHERE name=%s", (phone, name))
        print("Phone updated.")
    else:
        cur.execute("INSERT INTO phonebook (name, surname, phone) VALUES (%s, '', %s)", (name, phone))
        print("User inserted.")
    conn.commit()

def bulk_insert_users():
    n=int(input("How many users you want to insert ?: "))
    invalid=[]
    for _ in range(n):
        name=input("Enter name: ")
        phone=input("Enter phone: ")
        if not phone.isdigit():
            invalid.append((name, phone))
            continue
        cur.execute("SELECT * FROM phonebook WHERE name=%s", (name,))
        if cur.fetchall():
            cur.execute("UPDATE phonebook SET phone=%s WHERE name=%s", (phone, name))
        else:
            cur.execute("INSErT INTO phonebook (name, surname, phone) VALUES(%s, '', %s)", (name, phone))
    conn.commit()
    if invalid:
        print("Invalid phone numbers:")
        for entry in invalid:
            print(entry)
    
def paginate_query():
    limit=int(input("Enter limit: "))
    offset=int(input("Enter offset: "))
    cur.execute("SELECT * FROM phonebook ORDER BY user_id LIMIT %s OFFSET %s", (limit, offset))
    results=cur.fetchall()
    print(tabulate(results, headers=["ID", "Name", "Surname", "Phone"], tablefmt='fancy_grid'))

def delete_by_name_or_phone():
    value=input("Enter name or phone to delete: ")
    cur.execute("DELETE FROM phonebook WHERE name=%s OR phone=%s", (value, value))
    conn.commit()
    print("Deleted(if existed)")

def show_all():
    cur.execute("SELECT * FROM phonebook")
    rows=cur.fetchall()
    print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"], tablefmt='fancy_grid'))

def print_menu():
    print("""
=== Phonebook Lab11 Menu ===
1.[pattern] - Search by pattern
2.[insert] - Insert or update user
3. [bulk]    - Insert many users with validation
4. [page]    - Paginated query
5. [delete]  - Delete by name or phone
6. [show]    - Show all data
7. [exit]    - Exit
""")

while True:
    print_menu()
    command=input("Enter command: ").strip().lower()
    
    if command=="pattern":
        search_by_pattern()
    elif command=="insert":
        insert_or_update_user()
    elif command=="bulk":
        bulk_insert_users()
    elif command=="page":
        paginate_query()
    elif command=="delete":
        delete_by_name_or_phone()
    elif command=="show":
        show_all()
    elif command=="exit":
        break
    else:
        print("Unknown command.")

cur.close()
conn.close()