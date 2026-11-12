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




def test_delete():
    if os.path.exists("test_expenses.db"):
        os.remove("test_expenses.db")

    storage.init_db()
    storage.add_expense_db(
        {"amount": 10.0, "category": "food", "description": "a", "date": "2026-09-28"}
    )
    storage.add_expense_db(
        {"amount": 20.0, "category": "game", "description": "b", "date": "2026-09-28"}
    )

    first = storage.get_all_expenses_db()[0]
    storage.delete_expense_db(first["id"])
    result = storage.get_all_expenses_db()

    assert len(result) == 1
    assert result[0]["category"] == "game"

    os.remove("test_expenses.db")

test_add_and_get()
test_delete()

print("Storage tests passed!")