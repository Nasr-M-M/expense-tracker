import json

import sqlite3
DB_NAME = "expenses.db"
ALLOWED_FIELDS = {"amount", "category", "description", "date"}

def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            description TEXT NOT NULL,
            date TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def add_expense_db(expense):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO expenses (amount, category, description, date) VALUES (?, ?, ?, ?)",
        (
            expense["amount"],
            expense["category"],
            expense["description"],
            expense["date"],
        ),
    )
    conn.commit()
    conn.close()


def get_all_expenses_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, amount, category, description, date FROM expenses")
    rows = cursor.fetchall()
    conn.close()

    expenses = []
    for row in rows:
        expenses.append({
            "id": row[0],
            "amount": row[1],
            "category": row[2],
            "description": row[3],
            "date": row[4],
        })
    return expenses


def delete_expense_db(expense_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    conn.commit()
    conn.close()





def update_expense_db(expense_id, field, new_value):
    if field not in ALLOWED_FIELDS:
        raise ValueError(f"Invalid field: {field}")

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        f"UPDATE expenses SET {field} = ? WHERE id = ?",
        (new_value, expense_id),
    )
    conn.commit()
    conn.close()

def find_by_category_db(category):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, amount, category, description, date FROM expenses "
        "WHERE LOWER(TRIM(category)) = LOWER(TRIM(?))",
        (category,),
    )
    rows = cursor.fetchall()
    conn.close()

    return [
        {"id": r[0], "amount": r[1], "category": r[2], "description": r[3], "date": r[4]}
        for r in rows
    ]

def migrate_json_to_db():
    expenses = load_expenses()
    for item in expenses:
        add_expense_db(item)
    return len(expenses)

if __name__ == "__main__":
    init_db()
    delete_expense_db(1)
    delete_expense_db(3)
    print(get_all_expenses_db())