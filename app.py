from flask import Flask, render_template, request, redirect
from expenses import CURRENCY
from storage import init_db, get_all_expenses_db, add_expense_db

app = Flask(__name__)


@app.route("/expenses")
def expenses_page():
    expenses = get_all_expenses_db()
    return render_template("expenses.html", expenses=expenses, currency=CURRENCY)


@app.route("/add", methods=["POST"])
def add_page():
    expense = {
        "amount": float(request.form["amount"]),
        "category": request.form["category"],
        "description": request.form["description"],
        "date": request.form["date"],
    }
    add_expense_db(expense)
    return redirect("/expenses")


if __name__ == "__main__":
    init_db()
    app.run(debug=True)