from datetime import date
import json
import math
from storage import load_expenses, save_expenses

CURRENCY = "SAR"





expenses = load_expenses()
    

 
def format_expense(item):
    return f"{item['category']} - {item['description']} - {item['amount']:.2f} {CURRENCY} - {item['date']}"

def display_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    for i, item in enumerate(expenses, start=1):
        print(f"{i}. {format_expense(item)}")



def get_amount():
    while True:
        try:
            amount = float(input("Amount: "))

            if amount > 0 and math.isfinite(amount):
                return amount
            else:
                print("Amount must be a valid number.")

        except ValueError:
            print("Please enter a valid number.")


def get_text(prompt):
    while True:
        text = input(prompt)
        if text.strip() != "":
            return text
        else:
            print("This field cannot be empty.")


def add_expense(expenses):
    amount = get_amount()
    category = get_text("Category: ")
    description = get_text("Description: ")


            
    entry = {
        "amount": amount,
        "category": category,
        "description": description,
        "date": get_date() 
        }

    expenses.append(entry)




def get_date():
    while True:
        date_input = input("Date (press Enter for today): ")

        if not date_input:
            return date.today().isoformat()

        try:
            valid_date = date.fromisoformat(date_input)
            return valid_date.isoformat()

        except ValueError:
            print("Invalid date. Please use YYYY-MM-DD.")


def view_expenses(expenses):
    if expenses:
        if len(expenses) == 1:
            print(f"You have {len(expenses)} expense.")
        else:
            print(f"You have {len(expenses)} expenses.")

    display_expenses(expenses)




def show_total(expenses):
    total = 0
    for item in expenses:
        total += item["amount"]
    return total


def delete_expense(expenses):
    if not expenses:
        print("No expenses to delete.")
        return

    if len(expenses) == 1:
        print(f"You have {len(expenses)} expense.")
    else:
        print(f"You have {len(expenses)} expenses.")


    while True:
        display_expenses(expenses)

        try:
            number = int(input("Enter expense number to delete (or 0 to cancel): "))

            if number == 0:
                return

            if 1 <= number <= len(expenses):
                confirm = get_confirmation()

                if confirm == "y":
                    removed = expenses.pop(number - 1)
                    print(f"Deleted: {format_expense(removed)}")
                    break

                elif confirm == "n":
                    continue

                elif confirm == "c":
                    return

            else:
                print("Invalid expense number.")

        except ValueError:
            print("Please enter a valid number.")


def get_confirmation():
    while True:
        confirm = input(
            "Delete this expense? (y = delete, n = back to list, c = cancel): "
        ).lower()

        if confirm in ["y", "n", "c"]:
            return confirm
        else:
            print("Please enter y, n, or c.")


def get_choice():
    while True:
        print("\n1. Add expense")
        print("2. View expenses")
        print("3. Delete expense")
        print("4. Show total")
        print("5. Search by category")
        print("6. Edit expense")
        print("7. Exit")
    
        try:
            choice = int(input("Choose: "))
            if 1 <= choice <= 7:
                return choice
            else:
                print("Please choose a number from 1 to 7.")
        except ValueError:
            print("Please put a valid number.")

def find_by_category(expenses, category):
    results = []
    for item in expenses:
        if item["category"].strip().lower() == category.strip().lower():
            results.append(item)
    return results   

    

def search_by_category(expenses):
    if not expenses:
        print("There are no expenses to search.")
        return
    category = get_text("Enter category to search: ")
    result = find_by_category(expenses, category)
    if not result:
        print(f"No expenses found in category '{category}'.")
    else:
        display_expenses(result)


def get_edit_choice():
    while True:
        try:
            choice = int(input("Choose: "))

            if 1 <= choice <= 5:
                return choice
            else:
                print("Please choose a number from 1 to 5.")

        except ValueError:
            print("Please put a valid number.")


def edit_expense(expenses):
    if not expenses:
        print("No expenses to edit.")
        return

    while True:
        display_expenses(expenses)

        try:
            number = int(input("Enter expense number to edit (or 0 to cancel): "))
            if number == 0:
                return
            if not 1 <= number <= len(expenses):
                print("Invalid expense number.")
                continue
        except ValueError:
            print("Please put a valid number.")
            continue

        expense = expenses[number - 1]
        print("1. Amount")
        print("2. Category")
        print("3. Description")
        print("4. Date")
        print("5. Cancel")
        choice = get_edit_choice()

        if choice == 1:
            expense["amount"] = get_amount()
        elif choice == 2:
            expense["category"] = get_text("Category: ")
        elif choice == 3:
            expense["description"] = get_text("Description: ")
        elif choice == 4:
            expense["date"] = get_date()
        else:
            return

        print("Expense updated successfully.")
        save_expenses(expenses)
        return












if __name__ == "__main__":
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


