from flask import Flask, render_template, request, redirect, abort
from expenses import CURRENCY, validate_amount, validate_text, validate_date
from storage import (
    init_db, get_all_expenses_db, add_expense_db,
    delete_expense_db, get_expense_db,update_expense_full_db
)

app = Flask(__name__)

@app.route("/")
def home():
    return redirect("/expenses")


@app.route("/expenses")
def expenses_page():
    expenses = get_all_expenses_db()
    return render_template("expenses.html", expenses=expenses, currency=CURRENCY)


@app.route("/add", methods=["POST"])
def add_page():
    
    try:
        amount = validate_amount(request.form["amount"])
        category = validate_text(request.form["category"])
        description = validate_text(request.form["description"])
        date = validate_date(request.form["date"])
    except ValueError as error:
        return f"Invalid input: {error}", 400


    expense = {
        "amount": amount,
        "category": category,
        "description": description,
        "date": date,
    }
    add_expense_db(expense)

    return redirect("/expenses")

@app.route("/delete/<int:expense_id>", methods=["POST"])
def delete_page(expense_id):
    delete_expense_db(expense_id)
    return redirect("/expenses")

@app.route("/edit/<int:expense_id>", methods=["GET", "POST"])
def edit_page(expense_id):
    expense = get_expense_db(expense_id)
    if expense is None:
        abort(404)

    if request.method == "POST":
        try:
            amount = validate_amount(request.form["amount"])
            category = validate_text(request.form["category"])
            description = validate_text(request.form["description"])
            date = validate_date(request.form["date"])
        except ValueError as error:
            return f"Invalid input: {error}", 400

        update_expense_full_db(
            expense_id,
            {
                "amount": amount,
                "category": category,
                "description": description,
                "date": date,
            },
        )
        return redirect("/expenses")

    return render_template("edit.html", expense=expense)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)