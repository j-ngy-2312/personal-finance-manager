import sqlite3
import database

def add_expense(user_id, amount, category, date):
    try:
        conn = database.get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO expenses (user_id, amount, category, date) VALUES (?, ?, ?, ?)',
                       (user_id, amount, category, date))
        conn.commit()
        print("Expense added successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred while adding the expense: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        conn.close()

def edit_expense(expense_id, amount, category, date):
    try:
        conn = database.get_db_connection()
        cursor = conn.cursor()
        cursor.execute('UPDATE expenses SET amount = ?, category = ?, date = ? WHERE id = ?',
                       (amount, category, date, expense_id))
        conn.commit()
        print("Expense updated successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred while updating the expense: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        conn.close()

def delete_expense(expense_id):
    try:
        conn = database.get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM expenses WHERE id = ?', (expense_id,))
        conn.commit()
        print("Expense deleted successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred while deleting the expense: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        conn.close()
