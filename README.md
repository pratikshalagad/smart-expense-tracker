# Smart Expense Tracker

## Project Overview

Smart Expense Tracker is a web-based application that helps users record, categorize, and visualize their daily expenses. It provides a simple dashboard with graphical insights so users can better understand their spending habits.


## Features

* Add daily expenses
* Categorize expenses (Food, Travel, Shopping, etc.)
* Dashboard with category-wise visualization
* Lightweight database storage
* Simple and clean UI


## Tech Stack

| Layer          | Technology     | Purpose         |
| -------------- | -------------- | --------------- |
| Frontend       | HTML + CSS     | User Interface  |
| Frontend Logic | JavaScript     | Chart rendering |
| Backend        | Python (Flask) | Server logic    |
| Database       | SQLite         | Data storage    |
| Visualization  | Chart.js       | Expense graphs  |


## Project Structure

smart-expense-tracker/
│
├── app.py
├── database.db
├── templates/
│   ├── index.html
│   ├── add_expense.html
│   └── dashboard.html
└── venv/


##  Installation & Setup

### 1️] Clone repository

git clone https://github.com/pratikshalagad/smart-expense-tracker.git
cd smart-expense-tracker

### 2️] Create virtual environment

python -m venv venv
venv\Scripts\activate

### 3️] Install dependencies

pip install flask

### 4️] Run application

py app.py

### 5️] Open in browser

http://127.0.0.1:5000


## How It Works

1. User enters expense details.
2. Flask receives form data.
3. Data is stored in SQLite database.
4. Dashboard fetches totals per category.
5. Chart.js renders pie chart visualization.


## Use Case

This project demonstrates full-stack development skills including:

* Backend logic
* Database handling
* Template rendering
* Data visualization

## Future Improvements

* User authentication
* Monthly reports
* Export to Excel/PDF
* AI spending insights
* REST API support

## Author

**Pratiksha Lagad**


This project is open source and available under the MIT License.
