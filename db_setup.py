import sqlite3
import psycopg2

MSG = ""    #used for message sent to user e.g. successful installation or db connection failed or any other error

def sqlite_db_creation(db_name):
    global MSG
    my_db_name = db_name
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
        MSG = f"Database {my_db_name} successfully created."
    except:
        MSG = "Error while creating the table"

    con.close()
    return MSG


def postgresql_db_creation(db_name):
    global MSG
    my_db_name = db_name
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="",
    )
    conn.autocommit = True
    cur = conn.cursor()
    try:
        cur.execute(f"CREATE DATABASE {db_name};")
        MSG = "Database successfully created."
    except psycopg2.errors.DuplicateDatabase:
        MSG = "Database already exists"


    cur.close()
    conn.close()

    conn = psycopg2.connect(
        host="localhost",
        database=db_name,
        user="postgres",
        password="",
    )

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
    try:
        cur.execute(sql)
        MSG = MSG + " " + "Table successfully created."
    except psycopg2.errors.SyntaxError:
        MSG = "Syntax error while creating the table"

    conn.commit()
    cur.close()
    conn.close()

    return MSG