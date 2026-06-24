import os
import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS files (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename TEXT UNIQUE,
    content TEXT
)
""")

folder = "files"

if os.path.exists(folder):

    for file in os.listdir(folder):

        path = os.path.join(folder, file)

        if os.path.isfile(path):

            with open(path, "r", encoding="utf-8") as f:

                content = f.read()

                cursor.execute("""
                INSERT OR REPLACE INTO files (filename, content)
                VALUES (?, ?)
                """, (file, content))

conn.commit()
conn.close()

print("Files indexed successfully!")