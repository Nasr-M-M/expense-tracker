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

def test_update():
    if os.path.exists("test_expenses.db"):
        os.remove("test_expenses.db")

    storage.init_db()
    storage.add_expense_db(
        {"amount": 10.0, "category": "food", "description": "a", "date": "2026-09-28"}
    )

    item = storage.get_all_expenses_db()[0]
    storage.update_expense_db(item["id"], "amount", 99.0)
    result = storage.get_all_expenses_db()

    assert result[0]["amount"] == 99.0
    assert result[0]["category"] == "food"

    os.remove("test_expenses.db")


def test_update_invalid_field():
    if os.path.exists("test_expenses.db"):
        os.remove("test_expenses.db")

    storage.init_db()
    storage.add_expense_db(
        {"amount": 10.0, "category": "food", "description": "a", "date": "2026-09-28"}
    )

    try:
        storage.update_expense_db(1, "amount; DROP TABLE expenses", 5)
    except ValueError:
        return
    assert False, "Expected ValueError"


def test_find_by_category():
    if os.path.exists("test_expenses.db"):
        os.remove("test_expenses.db")

    storage.init_db()
    storage.add_expense_db(
        {"amount": 10.0, "category": "food", "description": "a", "date": "2026-09-28"}
    )
    storage.add_expense_db(
        {"amount": 20.0, "category": "game", "description": "b", "date": "2026-09-28"}
    )
    storage.add_expense_db(
        {"amount": 30.0, "category": "food", "description": "c", "date": "2026-09-28"}
    )

    result = storage.find_by_category_db("food")
    assert len(result) == 2

    result = storage.find_by_category_db("  FOOD ")
    assert len(result) == 2

    result = storage.find_by_category_db("xyz")
    assert result == []

    os.remove("test_expenses.db")