# Expense Management System - Mini Project Report

## 1. Introduction

The Expense Management System is a beginner-friendly Python application that helps users record and manage their daily expenses.

The system stores expense information in an SQLite database and provides a graphical interface using Tkinter.

## 2. Objectives

The objectives of the project are:

1. To create a simple digital expense tracker.
2. To understand Python programming.
3. To learn how a Python program communicates with a database.
4. To implement CRUD operations.
5. To create a basic graphical user interface.
6. To generate a simple spending summary.

## 3. Technologies

### Python

Python is used to implement the application logic.

### Tkinter

Tkinter is used to create the graphical user interface.

### SQLite

SQLite is used as the database because it is lightweight and does not require a separate database server.

## 4. Modules

### Main Module

The main module creates the user interface and connects user actions to database functions.

### Database Module

The database module performs SQL operations.

### Dashboard Module

The dashboard module displays summary information.

## 5. Database Design

The system contains an `expenses` table.

| Field | Type | Description |
|---|---|---|
| id | INTEGER | Unique expense ID |
| amount | REAL | Expense amount |
| category | TEXT | Expense category |
| date | TEXT | Date of expense |
| description | TEXT | Additional information |

## 6. CRUD Operations

### Create

The user enters expense details and clicks Add Expense.

### Read

The application retrieves stored expenses from SQLite and displays them in a table.

### Update

The user selects an existing expense, changes its details and clicks Update.

### Delete

The user selects an expense and clicks Delete.

## 7. Future Improvements

Possible future improvements include:

- User login
- Monthly budgets
- Export to CSV
- PDF reports
- Expense search
- Date filters
- Graphs and charts
- Cloud database
- Mobile application

## 8. Conclusion

The project demonstrates how Python, GUI programming and databases can be combined to create a useful application.

It is intentionally designed at a beginner-friendly level so that a first-year student can understand and explain the complete project.
