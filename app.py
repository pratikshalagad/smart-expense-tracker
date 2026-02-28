from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

# create table automatically
def create_table():
    conn = get_db()
    conn.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL,
        category TEXT,
        description TEXT,
        date TEXT
    )
    """)
    conn.close()

create_table()

# homepage
@app.route("/")
def index():
    conn = get_db()
    expenses = conn.execute("SELECT * FROM expenses").fetchall()
    conn.close()
    return render_template("index.html", expenses=expenses)

# add expense
@app.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        amount = request.form["amount"]
        category = request.form["category"]
        description = request.form["description"]
        date = request.form["date"]

        conn = get_db()
        conn.execute(
            "INSERT INTO expenses (amount, category, description, date) VALUES (?,?,?,?)",
            (amount, category, description, date)
        )
        conn.commit()
        conn.close()
        return redirect("/")

    return render_template("add_expense.html")

# dashboard
@app.route("/dashboard")
def dashboard():
    conn = get_db()

    data = conn.execute(
        "SELECT category, SUM(amount) as total FROM expenses GROUP BY category"
    ).fetchall()

    total_spent = conn.execute(
        "SELECT SUM(amount) FROM expenses"
    ).fetchone()[0]

    conn.close()

    if total_spent is None:
        total_spent = 0

    categories = [row["category"] for row in data] if data else []
    totals = [row["total"] for row in data] if data else []

    highest_category = None
    highest_amount = 0

    if data:
        highest = max(data, key=lambda x: x["total"])
        highest_category = highest["category"]
        highest_amount = highest["total"]

    return render_template(
        "dashboard.html",
        categories=categories,
        totals=totals,
        total_spent=total_spent,
        highest_category=highest_category,
        highest_amount=highest_amount
    )

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)