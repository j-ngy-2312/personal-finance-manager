import auth
import expenses
import income
import budget
import reports
import database

def main():
    database.init_db()
    print("Welcome to Personal Finance Manager!")
    while True:
        print("1. Register")
        print("2. Login")
        choice = input("Choose an option: ")
        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            if auth.register(username, password):
                print("Registration successful.")
            else:
                print("Username already exists.")
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            user_id = auth.login(username, password)
            if user_id:
                print("Login successful.")
                while True:
                    print("1. Add Expense")
                    print("2. Edit Expense")
                    print("3. Delete Expense")
                    print("4. Add Income")
                    print("5. Edit Income")
                    print("6. Delete Income")
                    print("7. Set Budget")
                    print("8. Generate Report")
                    print("9. Logout")
                    choice = input("Choose an option: ")
                    if choice == '1':
                        amount = float(input("Enter amount: "))
                        category = input("Enter category: ")
                        date = input("Enter date (YYYY-MM-DD): ")
                        expenses.add_expense(user_id, amount, category, date)
                    elif choice == '2':
                        expense_id = int(input("Enter expense ID: "))
                        amount = float(input("Enter new amount: "))
                        category = input("Enter new category: ")
                        date = input("Enter new date (YYYY-MM-DD): ")
                        expenses.edit_expense(expense_id, amount, category, date)
                    elif choice == '3':
                        expense_id = int(input("Enter expense ID: "))
                        expenses.delete_expense(expense_id)
                    elif choice == '4':
                        amount = float(input("Enter amount: "))
                        source = input("Enter source: ")
                        date = input("Enter date (YYYY-MM-DD): ")
                        income.add_income(user_id, amount, source, date)
                    elif choice == '5':
                        income_id = int(input("Enter income ID: "))
                        amount = float(input("Enter new amount: "))
                        source = input("Enter new source: ")
                        date = input("Enter new date (YYYY-MM-DD): ")
                        income.edit_income(income_id, amount, source, date)
                    elif choice == '6':
                        income_id = int(input("Enter income ID: "))
                        income.delete_income(income_id)
                    elif choice == '7':
                        category = input("Enter category: ")
                        amount = float(input("Enter amount: "))
                        budget.set_budget(user_id, category, amount)
                    elif choice == '8':
                        expenses_data, income_data = reports.generate_report(user_id)
                        reports.plot_expenses(expenses_data)
                    elif choice == '9':
                        break
            else:
                print("Invalid credentials.")

if __name__ == "__main__":
    main()
