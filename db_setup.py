import sqlite3
import psycopg2

MSG = ""    #used for message sent to user e.g. successful installation or db connection failed or any other error

def sqlite_db_creation(db_name):
    global MSG
    my_db_name = db_name+".db"
    con = sqlite3.connect(my_db_name)
    cur = con.cursor()
    try:
        cur.execute(
            "CREATE TABLE assets ("
            "asset_id INTEGER PRIMARY KEY AUTOINCREMENT, "
            "asset_tag TEXT NOT NULL UNIQUE, "
            "asset_type TEXT NOT NULL, "
            "serial_number TEXT, "
            "purchase_date TEXT, "
            "warranty_expiry TEXT, "
            "vendor_name TEXT, "
            "assigned_to TEXT, "
            "location TEXT, "
            "status TEXT CHECK (status IN ('Active', 'Retired', 'In Repair', 'Lost')), "
            "notes TEXT"
            ");"
        )
        MSG = f"Database {my_db_name} and table assets were successfully created."
    except:
        MSG = "Error while creating the table"

    con.close()
    return MSG


def postgresql_db_creation(db_name):
    global MSG
    my_db_name = db_name
    with  psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="temppa55",
        ) as conn:
        conn.autocommit = True

        with conn.cursor() as cur:
            try:
                cur.execute(f"CREATE DATABASE {my_db_name};")
                MSG = "Database successfully created."
            except psycopg2.errors.DuplicateDatabase:
                MSG = "Database already exists"
            except psycopg2.Error as e:
                MSG = f"Database creation failed: {e}"

    with psycopg2.connect(
        host="localhost",
        database=db_name,
        user="postgres",
        password="temppa55",
    ) as conn:
        sql = """
            CREATE TABLE IF NOT EXISTS assets (
                asset_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                asset_tag VARCHAR(50) NOT NULL UNIQUE,
                asset_type VARCHAR(50) NOT NULL,
                serial_number VARCHAR(100),
                purchase_date DATE,
                warranty_expiry DATE,
                vendor_name VARCHAR(100),
                assigned_to VARCHAR(100),
                location VARCHAR(100),
                status VARCHAR(20)
                    CHECK (status IN ('Active', 'Retired', 'In Repair', 'Lost')),
                notes TEXT
            );
            """
        with conn.cursor() as cur:
            try:
                cur.execute(sql)
                MSG += " Table successfully created."
            except psycopg2.Error as e:
                MSG += f"Table creation failed: {e}"

    return MSG