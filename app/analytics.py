import sqlite3
from datetime import datetime

def log_query(query, response_time):
    conn = sqlite3.connect("analytics.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS queries (
            id INTEGER PRIMARY KEY,
            query TEXT,
            response_time REAL,
            timestamp TEXT
        )
    """)
    cursor.execute("INSERT INTO queries (query, response_time, timestamp) VALUES (?, ?, ?)",
                   (query, response_time, datetime.now()))
    conn.commit()
    conn.close()
