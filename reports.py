import sqlite3
import database
import matplotlib.pyplot as plt

def generate_report(user_id):
    try:
        conn = database.get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM expenses WHERE user_id = ?', (user_id,))
        expenses = cursor.fetchall()
        cursor.execute('SELECT * FROM income WHERE user_id = ?', (user_id,))
        income = cursor.fetchall()
        return expenses, income
    except sqlite3.Error as e:
        print(f"An error occurred while generating the report: {e}")
        return [], []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return [], []
    finally:
        if conn:
            conn.close()

def plot_expenses(expenses):
    try:
        categories = [expense['category'] for expense in expenses]
        amounts = [expense['amount'] for expense in expenses]
        plt.bar(categories, amounts)
        plt.xlabel('Categories')
        plt.ylabel('Amount')
        plt.title('Expenses Breakdown')
        plt.show()
    except KeyError as e:
        print(f"Data error: missing key {e}")
    except ValueError as e:
        print(f"Data error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while plotting expenses: {e}")
