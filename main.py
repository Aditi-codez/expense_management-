import tkinter as tk
from tkinter import ttk, messagebox
from database import initialize_database, add_expense, get_expenses, update_expense, delete_expense, get_summary
from dashboard import show_dashboard


class ExpenseManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Management System")
        self.root.geometry("950x650")
        self.root.resizable(False, False)

        self.selected_id = None

        self.setup_style()
        self.create_widgets()
        self.load_expenses()
        self.update_summary()

    def setup_style(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", rowheight=28, font=("Arial", 10))
        style.configure("Treeview.Heading", font=("Arial", 10, "bold"))
        style.configure("Title.TLabel", font=("Arial", 22, "bold"))
        style.configure("Summary.TLabel", font=("Arial", 11, "bold"))

    def create_widgets(self):
        title = ttk.Label(self.root, text="Expense Management System", style="Title.TLabel")
        title.pack(pady=15)

        form = ttk.LabelFrame(self.root, text="Expense Details", padding=15)
        form.pack(fill="x", padx=20, pady=5)

        ttk.Label(form, text="Amount:").grid(row=0, column=0, padx=8, pady=8, sticky="w")
        self.amount_entry = ttk.Entry(form, width=20)
        self.amount_entry.grid(row=0, column=1, padx=8, pady=8)

        ttk.Label(form, text="Category:").grid(row=0, column=2, padx=8, pady=8, sticky="w")
        self.category_box = ttk.Combobox(
            form,
            width=18,
            values=["Food", "Travel", "Shopping", "Education", "Bills", "Entertainment", "Health", "Other"],
            state="readonly"
        )
        self.category_box.grid(row=0, column=3, padx=8, pady=8)
        self.category_box.set("Food")

        ttk.Label(form, text="Date (YYYY-MM-DD):").grid(row=1, column=0, padx=8, pady=8, sticky="w")
        self.date_entry = ttk.Entry(form, width=20)
        self.date_entry.grid(row=1, column=1, padx=8, pady=8)

        ttk.Label(form, text="Description:").grid(row=1, column=2, padx=8, pady=8, sticky="w")
        self.description_entry = ttk.Entry(form, width=20)
        self.description_entry.grid(row=1, column=3, padx=8, pady=8)

        button_frame = ttk.Frame(form)
        button_frame.grid(row=0, column=4, rowspan=2, padx=20)

        ttk.Button(button_frame, text="Add Expense", command=self.add).pack(pady=3, fill="x")
        ttk.Button(button_frame, text="Update", command=self.update).pack(pady=3, fill="x")
        ttk.Button(button_frame, text="Delete", command=self.delete).pack(pady=3, fill="x")
        ttk.Button(button_frame, text="Clear", command=self.clear_form).pack(pady=3, fill="x")

        table_frame = ttk.LabelFrame(self.root, text="Expenses", padding=10)
        table_frame.pack(fill="both", expand=True, padx=20, pady=10)

        columns = ("id", "amount", "category", "date", "description")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=12)

        headings = {
            "id": "ID",
            "amount": "Amount",
            "category": "Category",
            "date": "Date",
            "description": "Description"
        }

        widths = {"id": 50, "amount": 100, "category": 140, "date": 120, "description": 350}

        for column in columns:
            self.tree.heading(column, text=headings[column])
            self.tree.column(column, width=widths[column], anchor="center")

        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.tree.bind("<<TreeviewSelect>>", self.select_expense)

        bottom = ttk.Frame(self.root)
        bottom.pack(fill="x", padx=20, pady=5)

        self.summary_label = ttk.Label(bottom, text="", style="Summary.TLabel")
        self.summary_label.pack(side="left")

        ttk.Button(
            bottom,
            text="Open Dashboard",
            command=lambda: show_dashboard(self.root)
        ).pack(side="right")

    def validate(self):
        amount = self.amount_entry.get().strip()
        category = self.category_box.get().strip()
        date = self.date_entry.get().strip()
        description = self.description_entry.get().strip()

        if not amount or not category or not date:
            messagebox.showwarning("Missing Data", "Please enter amount, category and date.")
            return None

        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid Amount", "Amount must be a positive number.")
            return None

        return amount, category, date, description

    def add(self):
        data = self.validate()
        if data:
            add_expense(*data)
            self.clear_form()
            self.load_expenses()
            self.update_summary()
            messagebox.showinfo("Success", "Expense added successfully.")

    def update(self):
        if self.selected_id is None:
            messagebox.showwarning("Select Expense", "Please select an expense to update.")
            return

        data = self.validate()
        if data:
            update_expense(self.selected_id, *data)
            self.clear_form()
            self.load_expenses()
            self.update_summary()
            messagebox.showinfo("Success", "Expense updated successfully.")

    def delete(self):
        if self.selected_id is None:
            messagebox.showwarning("Select Expense", "Please select an expense to delete.")
            return

        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this expense?"):
            delete_expense(self.selected_id)
            self.clear_form()
            self.load_expenses()
            self.update_summary()
            messagebox.showinfo("Success", "Expense deleted successfully.")

    def select_expense(self, event):
        selected = self.tree.selection()
        if not selected:
            return

        values = self.tree.item(selected[0], "values")
        self.selected_id = int(values[0])

        self.amount_entry.delete(0, tk.END)
        self.amount_entry.insert(0, values[1])

        self.category_box.set(values[2])

        self.date_entry.delete(0, tk.END)
        self.date_entry.insert(0, values[3])

        self.description_entry.delete(0, tk.END)
        self.description_entry.insert(0, values[4])

    def clear_form(self):
        self.selected_id = None
        self.amount_entry.delete(0, tk.END)
        self.category_box.set("Food")
        self.date_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        self.tree.selection_remove(self.tree.selection())

    def load_expenses(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for expense in get_expenses():
            self.tree.insert("", tk.END, values=expense)

    def update_summary(self):
        total, count = get_summary()
        self.summary_label.config(
            text=f"Total Expenses: ₹{total:.2f}    |    Number of Expenses: {count}"
        )


if __name__ == "__main__":
    initialize_database()

    root = tk.Tk()
    app = ExpenseManager(root)
    root.mainloop()
