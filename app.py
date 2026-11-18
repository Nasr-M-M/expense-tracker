from flask import Flask, render_template
from expenses import CURRENCY
from storage import init_db, get_all_expenses_db

app = Flask(__name__)


@app.route("/expenses")
def expenses_page():
    expenses = get_all_expenses_db()
    return render_template("expenses.html", expenses=expenses, currency=CURRENCY)


if __name__ == "__main__":
    init_db()
    app.run(debug=True)