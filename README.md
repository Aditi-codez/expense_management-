# Expense Management System

A simple Expense Management System made using Python, Tkinter and SQLite.

## Features

- Add expenses
- View all expenses
- Update expenses
- Delete expenses
- Category selection
- Expense summary
- Category-wise spending dashboard
- Data stored permanently in SQLite

## Technologies Used

- Python
- Tkinter
- SQLite
- SQL

## Project Structure

```text
ExpenseManagementSystem/
│
├── main.py
├── database.py
├── dashboard.py
├── requirements.txt
├── README.md
└── expenses.db
```

## How to Run

### 1. Install Python

Install Python 3 from the official Python website.

### 2. Open the project folder

Open Command Prompt or Terminal in this folder.

### 3. Run the program

```bash
python main.py
```

The program will automatically create the SQLite database and the `expenses` table.

## How It Works

The application has three main parts:

### main.py

Contains the main Tkinter window and user interface.

It handles:

- Adding expenses
- Updating expenses
- Deleting expenses
- Displaying expenses
- Reading user input

### database.py

Handles all communication with SQLite.

It contains functions for:

- Creating the database table
- Inserting data
- Reading data
- Updating data
- Deleting data
- Calculating totals

### dashboard.py

Displays a simple dashboard containing:

- Total spending
- Number of expenses
- Category-wise spending

## Database Table

The application uses the following table:

```sql
CREATE TABLE expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL NOT NULL,
    category TEXT NOT NULL,
    date TEXT NOT NULL,
    description TEXT
);
```

## Example

An expense could look like:

| ID | Amount | Category | Date | Description |
|---|---:|---|---|---|
| 1 | 250 | Food | 2026-09-29 | Lunch |
| 2 | 500 | Travel | 2026-09-28 | Bus ticket |
| 3 | 1200 | Shopping | 2026-09-25 | Clothes |

## Concepts Demonstrated

This project demonstrates beginner-level:

- Python functions
- Modules
- Classes
- Tkinter GUI
- SQLite database
- SQL queries
- CRUD operations
- Exception handling
- Basic data analysis

## CRUD

CRUD means:

- **Create** → Add an expense
- **Read** → View expenses
- **Update** → Edit an expense
- **Delete** → Remove an expense

This is the main database concept demonstrated by the project.
