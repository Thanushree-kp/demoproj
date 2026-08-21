# init_db.py
# Optional helper script: run this file ONCE to manually create
# the SQLite database and the 'students' table.
#
# Usage:
#   python init_db.py
#
# Note: app.py already creates the database automatically when it
# starts, so running this file is optional — it's here in case you
# want to set up (or reset) the database separately.

import sqlite3

DATABASE = "database.db"

conn = sqlite3.connect(DATABASE)

conn.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        course TEXT NOT NULL,
        age INTEGER NOT NULL
    )
""")

conn.commit()
conn.close()

print("Database and 'students' table created successfully (database.db)")
