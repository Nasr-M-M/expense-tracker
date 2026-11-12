import os
import storage

storage.DB_NAME = "test_expenses.db"


def test_add_and_get():
    if os.path.exists("test_expenses.db"):
        os.remove("test_expenses.db")

    storage.init_db()
    storage.add_expense_db(
        {"amount": 60.0, "category": "food", "description": "lunch", "date": "2026-09-28"}
    )
    result = storage.get_all_expenses_db()

    assert len(result) == 1
    assert result[0]["category"] == "food"

    os.remove("test_expenses.db")


test_add_and_get()
print("Storage tests passed!")