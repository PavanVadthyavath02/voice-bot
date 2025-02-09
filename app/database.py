import sqlite3

def get_account_balance(user_id):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT balance FROM users WHERE id=?", (user_id,))
    result = cursor.fetchone()

    conn.close()
    
    return result[0] if result else "Not found"
