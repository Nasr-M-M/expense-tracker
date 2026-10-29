from expenses import (
    get_choice, add_expense, view_expenses, delete_expense,
    show_total, search_by_category, edit_expense, CURRENCY,
)
from storage import init_db, get_all_expenses_db, save_expenses




if __name__ == "__main__":

    init_db()
    expenses = get_all_expenses_db()

    choice = get_choice()
    while choice != 7:
        if choice == 1:
            add_expense(expenses)
            save_expenses(expenses)

        elif choice == 2:
            view_expenses(expenses)

        elif choice == 3:
            delete_expense(expenses)
            save_expenses(expenses)

        elif choice == 4:
            total = show_total(expenses)
            if not expenses:
                print("No expenses found.")
            else:
                print(f"Total: {total:.2f} {CURRENCY}")
        elif choice == 5:
            search_by_category(expenses)
        elif choice == 6:
            edit_expense(expenses)

        
        choice = get_choice()
