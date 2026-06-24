import sqlite3
import time

def search_files(query):

    start = time.time()

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

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

    print("Search completed in:", end - start, "seconds")

    return results