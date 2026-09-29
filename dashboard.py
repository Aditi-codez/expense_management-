import tkinter as tk
from tkinter import ttk
from database import get_category_summary, get_summary


def show_dashboard(parent):
    window = tk.Toplevel(parent)
    window.title("Expense Dashboard")
    window.geometry("600x500")
    window.resizable(False, False)

    ttk.Label(
        window,
        text="Expense Dashboard",
        font=("Arial", 20, "bold")
    ).pack(pady=20)

    total, count = get_summary()

    summary = ttk.LabelFrame(window, text="Overall Summary", padding=20)
    summary.pack(fill="x", padx=30, pady=10)

    ttk.Label(
        summary,
        text=f"Total Spent: ₹{total:.2f}",
        font=("Arial", 13, "bold")
    ).pack(anchor="w", pady=5)

    ttk.Label(
        summary,
        text=f"Number of Expenses: {count}",
        font=("Arial", 13)
    ).pack(anchor="w", pady=5)

    category_frame = ttk.LabelFrame(
        window,
        text="Category-wise Spending",
        padding=10
    )
    category_frame.pack(fill="both", expand=True, padx=30, pady=10)

    tree = ttk.Treeview(
        category_frame,
        columns=("category", "amount"),
        show="headings",
        height=10
    )

    tree.heading("category", text="Category")
    tree.heading("amount", text="Amount")

    tree.column("category", width=250, anchor="center")
    tree.column("amount", width=200, anchor="center")

    tree.pack(fill="both", expand=True)

    for category, amount in get_category_summary():
        tree.insert("", tk.END, values=(category, f"₹{amount:.2f}"))
