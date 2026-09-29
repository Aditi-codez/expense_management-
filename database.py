import sqlite3

DATABASE_NAME = "expenses.db"


def get_connection():
    return sqlite3.connect(DATABASE_NAME)


def initialize_database():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL,
            description TEXT
        )
    """)

    connection.commit()
    connection.close()


def add_expense(amount, category, date, description):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO expenses (amount, category, date, description)
        VALUES (?, ?, ?, ?)
    """, (amount, category, date, description))

    connection.commit()
    connection.close()


def get_expenses():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, amount, category, date, description
        FROM expenses
        ORDER BY date DESC, id DESC
    """)

    expenses = cursor.fetchall()
    connection.close()
    return expenses


def update_expense(expense_id, amount, category, date, description):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE expenses
        SET amount = ?, category = ?, date = ?, description = ?
        WHERE id = ?
    """, (amount, category, date, description, expense_id))

    connection.commit()
    connection.close()


def delete_expense(expense_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))

    connection.commit()
    connection.close()


def get_summary():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT COALESCE(SUM(amount), 0), COUNT(*) FROM expenses")
    total, count = cursor.fetchone()

    connection.close()
    return total, count


def get_category_summary():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT category, SUM(amount)
        FROM expenses
        GROUP BY category
        ORDER BY SUM(amount) DESC
    """)

    data = cursor.fetchall()
    connection.close()
    return data
