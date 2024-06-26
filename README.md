# Personal Finance Manager

Personal Finance Manager is a command-line interface (CLI) application designed to help you manage your personal finances. You can track your income, expenses, and set budgets. Additionally, you can generate reports and visualize your expenses.

## Features
- User registration and login
- Add, edit, and delete expenses
- Add, edit, and delete income
- Set budgets for different categories
- Generate and display expense reports

## Prerequisites
- Python 3.x
- SQLite3
- Matplotlib

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/finance-manager.git
    cd finance-manager
    ```

2. **Install dependencies**:
    ```sh
    pip install bcrypt matplotlib
    ```

3. **Initialize the database**:
    The database will be automatically initialized when you first run the application.

## Usage

1. **Run the application**:
    ```sh
    python main.py
    ```

2. **Follow the on-screen instructions**:
    - Register a new user or login with an existing account.
    - Use the menu options to manage your finances.

## Project Structure

```
finance-manager/
├── database.py       # Database initialization and connection
├── auth.py           # User authentication (register and login)
├── expenses.py       # Expense management functions
├── income.py         # Income management functions
├── budget.py         # Budget management functions
├── reports.py        # Reporting and visualization
├── main.py           # Main application file with CLI interface
└── utils/
    └── hash_util.py  # Password hashing and checking utility functions
```

## Example Commands

- **Register a new user**:
  ```sh
  Enter username: user1
  Enter password: password
  Registration successful.
  ```

- **Login**:
  ```sh
  Enter username: user1
  Enter password: password
  Login successful.
  ```

- **Add an expense**:
  ```sh
  Enter amount: 50.75
  Enter category: Food
  Enter date (YYYY-MM-DD): 2024-05-01
  Expense added successfully.
  ```

- **Set a budget**:
  ```sh
  Enter category: Food
  Enter amount: 300
  Budget set successfully.
  ```

## Exception Handling

The application includes exception handling for common errors such as database connection issues, invalid user input, and more. If an error occurs, an appropriate message will be displayed to the user.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

- [SQLite](https://www.sqlite.org/)
- [Matplotlib](https://matplotlib.org/)
- [bcrypt](https://pypi.org/project/bcrypt/)

---

Replace `https://github.com/yourusername/finance-manager.git` with the actual URL of your GitHub repository. This README file provides a comprehensive overview of your project, including its features, installation instructions, usage examples, and more.
