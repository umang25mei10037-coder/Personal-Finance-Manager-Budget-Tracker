Personal Finance Manager & Budget Tracker 💰

A comprehensive, Python-based Command Line Interface (CLI) application designed to help students and young professionals track income, manage daily expenses, set budgets, and achieve savings goals effectively.

📋 Table of Contents

Features

Installation

Usage

Project Structure

Screenshots

Future Scope

Author

🚀 Features

📝 Transaction Logging: Record Income and Expenses with detailed metadata (Amount, Category, Description, Payment Method, Tags).

📊 Smart Budgeting: Set monthly limits for specific categories (e.g., Food, Transport). The system warns you if you cross 80% of your budget.

🎯 Savings Goals: Create custom goals (e.g., "New Phone") and track progress with visual bars. It calculates how much you need to save monthly to hit your deadline.

📉 Monthly Reports: Generate a "Report Card" for your finances, showing Total Income, Expenses, Net Savings, and Savings Rate.

💡 Intelligent Insights: Automated analysis of your spending patterns (e.g., "You spent 20% more on Food compared to last month").

💾 Data Persistence: All data is securely stored locally in finance_data.json, so you never lose your records.

🎨 Colorful UI: Uses terminal color codes for a visually appealing and easy-to-read interface.

🛠 Installation

Prerequisites:
Ensure you have Python installed on your system.

python --version


Run the Application:
No external libraries required! Just run:

python finance_manager.py


📖 Usage

The application runs in an interactive menu loop. Use the number keys to navigate.

Add Transaction: Select Option 1 (Income) or 2 (Expense).

Check Budgets: Select Option 7 to see ASCII progress bars of your budget usage.

Generate Report: Select Option 8 to see your monthly summary.

Data File: If finance_data.json doesn't exist, the app creates it automatically with sample data for demonstration.

📂 Project Structure

personal-finance-manager/
├── finance_manager.py    # Main application source code
├── finance_data.json     # Database file (Auto-generated)
├── README.md             # Project documentation



📸 Screenshots

(Optional: Add screenshots of your running code here)

Main Menu:

==================================================
   🎓 STUDENT FINANCE MANAGER v2.0   
==================================================
 1. Add Income 💰       6. Savings Goals 🎯
 2. Add Expense 💸      7. Insights 💡
 3. View History 📜     8. Search 🔍
 ...


Monthly Report Output:

Month: November 2025
Total Income: ₹ 8000.0
Total Expense: ₹ 1800.0
Net Savings : ₹ 6200.0


🔮 Future Scope

GUI: Implementation of a Graphical User Interface using Tkinter or PyQt.

Visualisation: Pie charts and bar graphs using matplotlib.

Export: Feature to export data to CSV or Excel format.

👤 Author

Name: [Umang Patel]
Registration No: 25MEI10037
Faculty: A.V.R. MAYURI
CSE1021


Course: Computer Science Engineering

This project was developed for the Semester 1 Python Programming Course
