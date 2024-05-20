import sqlite3
import database

def add_income(user_id, amount, source, date):
    try:
        conn = database.get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO income (user_id, amount, source, date) VALUES (?, ?, ?, ?)',
                       (user_id, amount, source, date))
        conn.commit()
        print("Income added successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred while adding the income: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        if conn:
            conn.close()

def edit_income(income_id, amount, source, date):
    try:
        conn = database.get_db_connection()
        cursor = conn.cursor()
        cursor.execute('UPDATE income SET amount = ?, source = ?, date = ? WHERE id = ?',
                       (amount, source, date, income_id))
        conn.commit()
        print("Income updated successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred while updating the income: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        if conn:
            conn.close()

def delete_income(income_id):
    try:
        conn = database.get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM income WHERE id = ?', (income_id,))
        conn.commit()
        print("Income deleted successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred while deleting the income: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        if conn:
            conn.close()
