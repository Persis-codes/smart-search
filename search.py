import sqlite3
import time

def search_files(query):

    start = time.time()

    try:

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS files (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT UNIQUE,
            content TEXT
        )
        """)

        cursor.execute("""
        SELECT filename, content,
        LENGTH(content) - LENGTH(REPLACE(content, ?, '')) as score
        FROM files
        WHERE content LIKE ?
        ORDER BY score DESC
        """, (query, '%' + query + '%'))

        results = cursor.fetchall()

        conn.close()

        end = time.time()

        print("Search completed in:", end - start)

        return results

    except Exception as e:

        print("ERROR:", e)

        return []