import sqlite3
import psycopg2

from main import DB_TYPE, CR_DB_NAME


def sqlite_db_creation():
    con = sqlite3.connect(CR_DB_NAME)
    cur = con.cursor()
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

    return True

def postgresql_db_creation():
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="",
    )
    conn.autocommit = True
    cur = conn.cursor()
    try:
        cur.execute(f"CREATE DATABASE {CR_DB_NAME};")
    except psycopg2.errors.DuplicateDatabase:
        print("Database already exists")

    cur.close()
    conn.close()

    conn = psycopg2.connect(
        host="localhost",
        database=CR_DB_NAME,
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

    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()

    print("Database and table created successfully.")

if DB_TYPE == "sqlite":
    is_db_created = sqlite_db_creation()
    if is_db_created:
        print("SQLite database if successfully created")
    else:
        print("SQLite database was not created")

elif DB_TYPE == "PostgreSQL":
    postgresql_db_creation()

