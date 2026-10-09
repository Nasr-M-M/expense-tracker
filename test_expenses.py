from unittest.mock import patch
from expenses import format_expense, get_amount, get_date, show_total , find_by_category

def test_format_expense():
    item = {
        "category": "food",
        "description": "lunch",
        "amount": 60,
        "date": "2026-09-28"
    }
    result = format_expense(item)
    print(result)
    assert result == "food - lunch - 60.00 SAR - 2026-09-28"

test_format_expense()



def test_show_total():
    expenses = [
        {"amount": 50.0, "category": "food", "description": "lunch", "date": "2026-09-28"},
        {"amount": 30.0, "category": "game", "description": "diablo", "date": "2026-09-25"},
    ]
    result = show_total(expenses)
    assert result == 80.0

test_show_total()

def test_get_amount():
    with patch('builtins.input', return_value='50'):
        result = get_amount()
        assert result == 50.0

test_get_amount()

def test_get_amount_retry():
    with patch('builtins.input', side_effect=['abc', '-5', '25']):
        result = get_amount()
        assert result == 25.0

test_get_amount_retry()

def test_get_date():
    with patch('builtins.input', return_value='2023-10-01'):
        result = get_date()
        assert result == '2023-10-01'

test_get_date()

def test_get_date_retry():
    with patch('builtins.input', side_effect=['2023/09/25', '2023.09.25', '2023-09-25']):
        result = get_date()
        assert result == '2023-09-25'

test_get_date_retry()

def test_find_by_category():
    expenses = [
        {"amount": 50.0, "category": "food", "description": "lunch", "date": "2026-09-28"},
        {"amount": 30.0, "category": "game", "description": "diablo", "date": "2026-09-25"},
        {"amount": 20.0, "category": "food", "description": "snack", "date": "2026-09-26"},
    ]
    result = find_by_category(expenses, 'food')
    assert len(result) == 2
    assert all(item['category'] == 'food' for item in result)
    
    result = find_by_category(expenses, "  FOOD ")
    assert len(result) == 2

    result = find_by_category(expenses, "xyz")
    assert result == []

test_find_by_category()

print("All tests passed!")