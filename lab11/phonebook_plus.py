import psycopg2

conn = psycopg2.connect(
    host="localhost",
    dbname="phonebook_db",
    user="postgres",
    password="070714"
)
cur = conn.cursor()

#1
search_by_temp = '''
CREATE OR REPLACE FUNCTION find_by_pattern(pattern TEXT)
RETURNS TABLE(id INT, name TEXT, phone TEXT) AS $$
BEGIN
    RETURN QUERY
    SELECT id, name, phone
    FROM phonebook
    WHERE name ILIKE '%' || pattern || '%' OR phone ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;
'''
cur.execute(search_by_temp)
conn.commit()

#2.
insert_update = '''
CREATE OR REPLACE PROCEDURE insert_or_update_user(p_name TEXT, p_phone TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE name = p_name) THEN
        UPDATE phonebook SET phone = p_phone WHERE name = p_name;
    ELSE
        INSERT INTO phonebook(name, phone) VALUES (p_name, p_phone);
    END IF;
END;
$$;
'''
cur.execute(insert_update)
conn.commit()

#3
insert_many = '''
CREATE OR REPLACE PROCEDURE insert_many_users(names TEXT[], phones TEXT[])
LANGUAGE plpgsql
AS $$
DECLARE
    i INT := 1;
    incorrect TEXT := '';
BEGIN
    WHILE i <= array_length(names, 1) LOOP
        IF phones[i] !~ '^[0-9]{10,15}$' THEN
            RAISE NOTICE 'Incorrect phone for user: % - %', names[i], phones[i];
        ELSE
            CALL insert_or_update_user(names[i], phones[i]);
        END IF;
        i := i + 1;
    END LOOP;
END;
$$;
'''
cur.execute(insert_many)
conn.commit()

#4
pagination = '''
CREATE OR REPLACE FUNCTION get_users_page(p_limit INT, p_offset INT)
RETURNS TABLE(id INT, name TEXT, phone TEXT) AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM phonebook ORDER BY id LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;
'''
cur.execute(pagination)
conn.commit()

#5
del_n_ph = '''
CREATE OR REPLACE PROCEDURE delete_by_value(p_val TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM phonebook WHERE name = p_val OR phone = p_val;
END;
$$;
'''
cur.execute(del_n_ph)
conn.commit()

def show_menu():
     print("\n1 - Search by pattern")
     print("2 - Insert or update one user")
     print("3 - Insert many users")
     print("4 - Pagination")
     print("5 - Delete user by name or phone")
     print("0 - Exit")
while True:
    show_menu()
    choice = input("Your choice: ")
    if choice == "0":
        break
    elif choice == "1":
        pattern = input("Enter pattern: ")
        cur.execute("SELECT * FROM find_by_pattern(%s)", (pattern,))
        for row in cur.fetchall():
            print(row)
    elif choice == "2":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        cur.execute("CALL insert_or_update_user(%s, %s)", (name, phone))
        conn.commit()
        print("Inserted or updated.")
    elif choice == "3":
        n = int(input("How many users? "))
        names = []
        phones = []
        for _ in range(n):
            names.append(input("Name: "))
            phones.append(input("Phone: "))
        cur.execute("CALL insert_many_users(%s, %s)", (names, phones))
        conn.commit()
    elif choice == "4":
        limit = int(input("Limit: "))
        offset = int(input("Offset: "))
        cur.execute("SELECT * FROM get_users_page(%s, %s)", (limit, offset))
        for row in cur.fetchall():
            print(row)
    elif choice == "5":
        val = input("Enter name or phone to delete: ")
        cur.execute("CALL delete_by_value(%s)", (val,))
        conn.commit()
        print("Deleted.")
cur.close()
conn.close()