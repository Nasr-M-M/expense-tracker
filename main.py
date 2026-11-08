from expenses import (
    get_choice, add_expense, view_expenses, delete_expense,
    show_total, search_by_category, edit_expense, CURRENCY
)
from storage import init_db, get_all_expenses_db, add_expense_db, delete_expense_db, update_expense_db




if __name__ == "__main__":

    init_db()
    expenses = get_all_expenses_db()

    choice = get_choice()
    while choice != 7:
        if choice == 1:
            entry = add_expense(expenses)
            add_expense_db(entry)

        elif choice == 2:
            view_expenses(expenses)

        elif choice == 3:
            removed = delete_expense(expenses)
            if removed:
                delete_expense_db(removed["id"])

        elif choice == 4:
            total = show_total(expenses)
            if not expenses:
                print("No expenses found.")
            else:
                print(f"Total: {total:.2f} {CURRENCY}")
        elif choice == 5:
            search_by_category(expenses)
        elif choice == 6:
             result = edit_expense(expenses)
             if result:
                expense_id, field, new_value = result
                update_expense_db(expense_id, field, new_value)

        
        choice = get_choice()
