import psycopg2
import csv
from config import host, user, password, db_name

def create_connection():
    conn = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name,
        port=31860
    )
    conn.autocommit = True
    return conn

def create_table():
    with create_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS phonebook (
                    id SERIAL PRIMARY KEY,
                    first_name VARCHAR(50) NOT NULL,
                    phone_number VARCHAR(50) UNIQUE NOT NULL
                );
            """)
            print("[INFO] Phonebook table created or already exists.")

def insert_manual(first_name, phone_number):
    with create_connection() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute(
                    "INSERT INTO phonebook (first_name, phone_number) VALUES (%s, %s);",
                    (first_name, phone_number)
                )
                print("[INFO] Contact added:", first_name, phone_number)
            except psycopg2.Error as e:
                print("[ERROR]", e)

def insert_from_csv(file_path):
    with create_connection() as conn:
        with conn.cursor() as cur:
            with open(file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    try:
                        cur.execute(
                            "INSERT INTO phonebook (first_name, phone_number) VALUES (%s, %s);",
                            (row[0], row[1])
                        )
                        conn.commit()
                    except psycopg2.IntegrityError:
                        conn.rollback()
                        print("[DUPLICATE] Skipped:", row)

def update_user(field, old_value, new_value):
    if field not in ['first_name', 'phone_number']:
        print("[ERROR] Field must be first_name or phone_number.")
        return
    with create_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                f"UPDATE phonebook SET {field} = %s WHERE {field} = %s;",
                (new_value, old_value)
            )
            print(f"[INFO] Updated: {field} = {old_value} → {new_value}")

def query_users(field=None, value=None):
    with create_connection() as conn:
        with conn.cursor() as cur:
            if field and value:
                cur.execute(
                    f"SELECT * FROM phonebook WHERE {field} ILIKE %s;",
                    ('%' + value + '%',)
                )
            else:
                cur.execute("SELECT * FROM phonebook;")
            for row in cur.fetchall():
                print(row)

def delete_user(field, value):
    if field not in ['first_name', 'phone_number']:
        print("[ERROR] Field must be first_name or phone_number.")
        return
    with create_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(f"DELETE FROM phonebook WHERE {field} = %s;", (value,))
            print(f"[INFO] Deleted by {field} = {value}")

# --- MENU ---
if __name__ == "__main__":
    create_table()
    
    while True:
        print("\n PHONEBOOK MENU")
        print("1. Add manually")
        print("2. Load from CSV")
        print("3. Update record")
        print("4. Search")
        print("5. Delete record")
        print("0. Exit")
        choice = input("Your choice: ")
        
        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            insert_manual(name, phone)

        elif choice == "2":
            path = input("Path to CSV file: ")
            insert_from_csv(path)

        elif choice == "3":
            field = input("Field to update (first_name/phone_number): ")
            old_val = input("Old value: ")
            new_val = input("New value: ")
            update_user(field, old_val, new_val)

        elif choice == "4":
            field = input("Filter (first_name/phone_number or Enter for all): ")
            if field:
                val = input("Value: ")
                query_users(field, val)
            else:
                query_users()

        elif choice == "5":
            field = input("Delete by (first_name/phone_number): ")
            val = input("Value: ")
            delete_user(field, val)

        elif choice == "0":
            print("Exit.")
            break

        else:
            print("[ERROR] Invalid input.")