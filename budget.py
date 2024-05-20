import sqlite3
import database

def set_budget(user_id, category, amount):
    try:
        conn = database.get_db_connection()
        cursor = conn.cursor()
        cursor.execute('REPLACE INTO budgets (user_id, category, amount) VALUES (?, ?, ?)',
                       (user_id, category, amount))
        conn.commit()
        print("Budget set successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred while setting the budget: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        if conn:
            conn.close()
