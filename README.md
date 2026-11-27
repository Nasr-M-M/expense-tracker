# Expense Tracker

A personal expense tracker built with Python. It has a command-line version and a web version that share the same SQLite database.

## Features
- Add, view, edit, and delete expenses (command line)
- Add, edit, and delete expenses from the web page
- Search by category and show the total
- Input validation shared by both versions
- Data saved in a SQLite database

## Project structure
- main.py: command-line menu
- app.py: Flask web app
- templates/expenses.html: the web page template
- expenses.py: expense logic and input validation
- storage.py: SQLite database functions
- test_expenses.py: tests for the logic and validation
- test_storage.py: tests for the database functions
- app.py: Flask web app
- templates/expenses.html: the main page template
- templates/edit.html: the edit page template

## How to run the command-line app
```
python main.py
```

## How to run the web app
```
pip install flask
python app.py
```
Then open http://127.0.0.1:5000


## How to run tests
```
pip install pytest
python -m pytest
```