import json
import datetime
from typing import List, Dict, Optional
import os
from collections import defaultdict

class FinanceManager:
    def __init__(self, filename='finance_data.json'):
        self.filename = filename
        self.data = self.load_data()
        self.expense_categories = ['Food', 'Transport', 'Entertainment', 'Shopping', 
                                   'Bills', 'Education', 'Healthcare', 'Others']
        self.income_categories = ['Salary', 'Freelance', 'Investment', 'Gift', 'Others']
    
    def load_data(self) -> Dict:
        """Load finance data from JSON file"""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return json.load(f)
        
        # Return default data with sample transactions for demonstration
        return {
            'transactions': [
                {
                    'id': 1,
                    'type': 'income',
                    'amount': 25000.00,
                    'category': 'Salary',
                    'description': 'Monthly internship stipend',
                    'date': '2025-11-01',
                    'payment_method': 'Bank Transfer',
                    'recurring': True,
                    'tags': ['work', 'monthly']
                },
                {
                    'id': 2,
                    'type': 'expense',
                    'amount': 3500.00,
                    'category': 'Education',
                    'description': 'Online course subscription - Python & ML',
                    'date': '2025-11-02',
                    'payment_method': 'Credit Card',
                    'recurring': False,
                    'tags': ['learning', 'investment']
                },
                {
                    'id': 3,
                    'type': 'expense',
                    'amount': 1200.00,
                    'category': 'Food',
                    'description': 'Groceries for the month',
                    'date': '2025-11-05',
                    'payment_method': 'Cash',
                    'recurring': False,
                    'tags': ['groceries', 'essential']
                },
                {
                    'id': 4,
                    'type': 'expense',
                    'amount': 500.00,
                    'category': 'Transport',
                    'description': 'Auto rickshaw and local bus fares',
                    'date': '2025-11-08',
                    'payment_method': 'Cash',
                    'recurring': False,
                    'tags': ['commute']
                },
                {
                    'id': 5,
                    'type': 'expense',
                    'amount': 800.00,
                    'category': 'Entertainment',
                    'description': 'Movie tickets and dinner with friends',
                    'date': '2025-11-10',
                    'payment_method': 'UPI',
                    'recurring': False,
                    'tags': ['social', 'weekend']
                },
                {
                    'id': 6,
                    'type': 'income',
                    'amount': 5000.00,
                    'category': 'Freelance',
                    'description': 'Web development project payment',
                    'date': '2025-11-12',
                    'payment_method': 'Bank Transfer',
                    'recurring': False,
                    'tags': ['freelance', 'side-hustle']
                },
                {
                    'id': 7,
                    'type': 'expense',
                    'amount': 2500.00,
                    'category': 'Shopping',
                    'description': 'New laptop accessories and books',
                    'date': '2025-11-15',
                    'payment_method': 'Debit Card',
                    'recurring': False,
                    'tags': ['tech', 'books']
                },
                {
                    'id': 8,
                    'type': 'expense',
                    'amount': 1800.00,
                    'category': 'Bills',
                    'description': 'Mobile recharge and internet bill',
                    'date': '2025-11-18',
                    'payment_method': 'UPI',
                    'recurring': True,
                    'tags': ['utility', 'monthly']
                },
                {
                    'id': 9,
                    'type': 'expense',
                    'amount': 600.00,
                    'category': 'Food',
                    'description': 'Restaurant dining - birthday celebration',
                    'date': '2025-11-20',
                    'payment_method': 'Credit Card',
                    'recurring': False,
                    'tags': ['dining', 'celebration']
                },
                {
                    'id': 10,
                    'type': 'expense',
                    'amount': 350.00,
                    'category': 'Transport',
                    'description': 'Weekly fuel for bike',
                    'date': '2025-11-21',
                    'payment_method': 'Cash',
                    'recurring': False,
                    'tags': ['fuel', 'vehicle']
                }
            ],
            'budgets': [
                {
                    'category': 'Food',
                    'monthly_limit': 5000.00,
                    'alert_threshold': 80,
                    'active': True
                },
                {
                    'category': 'Transport',
                    'monthly_limit': 2000.00,
                    'alert_threshold': 80,
                    'active': True
                },
                {
                    'category': 'Entertainment',
                    'monthly_limit': 3000.00,
                    'alert_threshold': 75,
                    'active': True
                },
                {
                    'category': 'Shopping',
                    'monthly_limit': 5000.00,
                    'alert_threshold': 80,
                    'active': True
                }
            ],
            'savings_goals': [
                {
                    'id': 1,
                    'name': 'Emergency Fund',
                    'target_amount': 50000.00,
                    'current_amount': 15000.00,
                    'deadline': '2026-03-31',
                    'priority': 'high',
                    'status': 'active'
                },
                {
                    'id': 2,
                    'name': 'Laptop Upgrade',
                    'target_amount': 80000.00,
                    'current_amount': 25000.00,
                    'deadline': '2026-06-30',
                    'priority': 'medium',
                    'status': 'active'
                },
                {
                    'id': 3,
                    'name': 'Vacation Trip',
                    'target_amount': 30000.00,
                    'current_amount': 8000.00,
                    'deadline': '2026-01-15',
                    'priority': 'low',
                    'status': 'active'
                }
            ],
            'investment_tracker': [
                {
                    'id': 1,
                    'name': 'Mutual Fund SIP',
                    'type': 'Mutual Fund',
                    'amount_invested': 10000.00,
                    'current_value': 10500.00,
                    'start_date': '2025-08-01',
                    'monthly_contribution': 2000.00
                }
            ]
        }
    
    def save_data(self):
        """Save finance data to JSON file"""
        with open(self.filename, 'w') as f:
            json.dump(self.data, f, indent=4)
    
    def add_transaction(self, trans_type: str, amount: float, category: str,
                       description: str, payment_method: str, recurring: bool = False,
                       tags: List[str] = None):
        """Add a new transaction (income or expense)"""
        transaction = {
            'id': len(self.data['transactions']) + 1,
            'type': trans_type.lower(),
            'amount': round(amount, 2),
            'category': category,
            'description': description,
            'date': str(datetime.date.today()),
            'payment_method': payment_method,
            'recurring': recurring,
            'tags': tags or []
        }
        self.data['transactions'].append(transaction)
        self.save_data()
        
        # Check budget alert if it's an expense
        if trans_type.lower() == 'expense':
            self.check_budget_alert(category)
        
        print(f"✓ {trans_type.capitalize()} of ₹{amount:,.2f} added successfully!")
    
    def view_transactions(self, filter_type: str = 'all', month: str = None):
        """Display transactions with filters"""
        transactions = self.data['transactions']
        
        # Filter by month if specified
        if month:
            transactions = [t for t in transactions if t['date'].startswith(month)]
        
        # Filter by type
        if filter_type != 'all':
            transactions = [t for t in transactions if t['type'] == filter_type]
        
        if not transactions:
            print("\nNo transactions found.")
            return
        
        # Sort by date (most recent first)
        transactions.sort(key=lambda x: x['date'], reverse=True)
        
        print("\n" + "="*90)
        print(f"TRANSACTIONS ({filter_type.upper()})")
        print("="*90)
        
        total = 0
        for trans in transactions:
            icon = "💰" if trans['type'] == 'income' else "💸"
            print(f"\n{icon} ID: {trans['id']} | Date: {trans['date']}")
            print(f"Amount: ₹{trans['amount']:,.2f} | Category: {trans['category']}")
            print(f"Description: {trans['description']}")
            print(f"Payment: {trans['payment_method']} | Recurring: {'Yes' if trans['recurring'] else 'No'}")
            if trans['tags']:
                print(f"Tags: {', '.join(trans['tags'])}")
            print("-"*90)
            
            if trans['type'] == 'income':
                total += trans['amount']
            else:
                total -= trans['amount']
        
        print(f"\nNet Total: ₹{total:,.2f}")
        print("="*90)
    
    def get_current_month_summary(self):
        """Get income and expense summary for current month"""
        current_month = datetime.date.today().strftime('%Y-%m')
        month_transactions = [t for t in self.data['transactions'] 
                            if t['date'].startswith(current_month)]
        
        total_income = sum(t['amount'] for t in month_transactions if t['type'] == 'income')
        total_expense = sum(t['amount'] for t in month_transactions if t['type'] == 'expense')
        
        return total_income, total_expense, month_transactions
    
    def generate_monthly_report(self):
        """Generate comprehensive monthly financial report"""
        print("\n" + "="*90)
        print("📊 MONTHLY FINANCIAL REPORT")
        print("="*90)
        
        current_month = datetime.date.today().strftime('%Y-%m')
        month_name = datetime.date.today().strftime('%B %Y')
        
        total_income, total_expense, month_transactions = self.get_current_month_summary()
        net_savings = total_income - total_expense
        savings_rate = (net_savings / total_income * 100) if total_income > 0 else 0
        
        print(f"\n📅 Period: {month_name}")
        print(f"\n💰 Total Income: ₹{total_income:,.2f}")
        print(f"💸 Total Expenses: ₹{total_expense:,.2f}")
        print(f"{'💚' if net_savings >= 0 else '❤️'} Net Savings: ₹{net_savings:,.2f}")
        print(f"📈 Savings Rate: {savings_rate:.1f}%")
        
        # Category-wise expense breakdown
        expense_by_category = defaultdict(float)
        for trans in month_transactions:
            if trans['type'] == 'expense':
                expense_by_category[trans['category']] += trans['amount']
        
        if expense_by_category:
            print(f"\n📂 Expense Breakdown by Category:")
            sorted_expenses = sorted(expense_by_category.items(), key=lambda x: x[1], reverse=True)
            for category, amount in sorted_expenses:
                percentage = (amount / total_expense * 100) if total_expense > 0 else 0
                bar = "█" * int(percentage / 2)
                print(f"   {category:15s}: ₹{amount:8,.2f} ({percentage:5.1f}%) {bar}")
        
        # Payment method analysis
        payment_methods = defaultdict(float)
        for trans in month_transactions:
            if trans['type'] == 'expense':
                payment_methods[trans['payment_method']] += trans['amount']
        
        if payment_methods:
            print(f"\n💳 Payment Method Usage:")
            for method, amount in sorted(payment_methods.items(), key=lambda x: x[1], reverse=True):
                print(f"   {method:15s}: ₹{amount:,.2f}")
        
        # Financial health indicators
        print(f"\n🏥 Financial Health Indicators:")
        if savings_rate >= 30:
            print("   ✅ Excellent savings rate! You're on track!")
        elif savings_rate >= 20:
            print("   👍 Good savings rate. Keep it up!")
        elif savings_rate >= 10:
            print("   ⚠️  Moderate savings. Try to reduce expenses.")
        else:
            print("   🚨 Low savings rate. Review your expenses urgently!")
        
        print("="*90)
    
    def set_budget(self, category: str, monthly_limit: float, alert_threshold: int = 80):
        """Set a budget limit for a category"""
        # Check if budget already exists
        for budget in self.data['budgets']:
            if budget['category'] == category:
                budget['monthly_limit'] = monthly_limit
                budget['alert_threshold'] = alert_threshold
                budget['active'] = True
                self.save_data()
                print(f"✓ Budget for {category} updated to ₹{monthly_limit:,.2f}")
                return
        
        # Add new budget
        budget = {
            'category': category,
            'monthly_limit': monthly_limit,
            'alert_threshold': alert_threshold,
            'active': True
        }
        self.data['budgets'].append(budget)
        self.save_data()
        print(f"✓ Budget for {category} set to ₹{monthly_limit:,.2f}")
    
    def check_budget_alert(self, category: str):
        """Check if budget limit is being approached for a category"""
        budget = next((b for b in self.data['budgets'] 
                      if b['category'] == category and b['active']), None)
        
        if not budget:
            return
        
        current_month = datetime.date.today().strftime('%Y-%m')
        month_expenses = sum(t['amount'] for t in self.data['transactions']
                           if t['type'] == 'expense' 
                           and t['category'] == category
                           and t['date'].startswith(current_month))
        
        percentage_used = (month_expenses / budget['monthly_limit'] * 100) if budget['monthly_limit'] > 0 else 0
        
        if percentage_used >= 100:
            print(f"\n🚨 BUDGET EXCEEDED for {category}!")
            print(f"   Spent: ₹{month_expenses:,.2f} / ₹{budget['monthly_limit']:,.2f}")
            print(f"   Over budget by: ₹{month_expenses - budget['monthly_limit']:,.2f}")
        elif percentage_used >= budget['alert_threshold']:
            print(f"\n⚠️  BUDGET ALERT for {category}!")
            print(f"   Spent: ₹{month_expenses:,.2f} / ₹{budget['monthly_limit']:,.2f} ({percentage_used:.1f}%)")
            print(f"   Remaining: ₹{budget['monthly_limit'] - month_expenses:,.2f}")
    
    def view_budget_status(self):
        """Display current budget status for all categories"""
        print("\n" + "="*90)
        print("💰 BUDGET STATUS - CURRENT MONTH")
        print("="*90)
        
        current_month = datetime.date.today().strftime('%Y-%m')
        
        for budget in self.data['budgets']:
            if not budget['active']:
                continue
            
            month_expenses = sum(t['amount'] for t in self.data['transactions']
                               if t['type'] == 'expense' 
                               and t['category'] == budget['category']
                               and t['date'].startswith(current_month))
            
            percentage_used = (month_expenses / budget['monthly_limit'] * 100) if budget['monthly_limit'] > 0 else 0
            remaining = budget['monthly_limit'] - month_expenses
            
            # Visual progress bar
            bar_length = 30
            filled = int(bar_length * min(percentage_used / 100, 1))
            bar = "█" * filled + "░" * (bar_length - filled)
            
            # Status icon
            if percentage_used >= 100:
                status = "🚨"
            elif percentage_used >= budget['alert_threshold']:
                status = "⚠️ "
            else:
                status = "✅"
            
            print(f"\n{status} {budget['category']}")
            print(f"   Budget: ₹{budget['monthly_limit']:,.2f}")
            print(f"   Spent:  ₹{month_expenses:,.2f} ({percentage_used:.1f}%)")
            print(f"   [{bar}]")
            print(f"   Remaining: ₹{remaining:,.2f}")
        
        print("="*90)
    
    def add_savings_goal(self, name: str, target_amount: float, 
                        deadline: str, priority: str = 'medium'):
        """Add a new savings goal"""
        goal = {
            'id': len(self.data['savings_goals']) + 1,
            'name': name,
            'target_amount': target_amount,
            'current_amount': 0.0,
            'deadline': deadline,
            'priority': priority.lower(),
            'status': 'active'
        }
        self.data['savings_goals'].append(goal)
        self.save_data()
        print(f"✓ Savings goal '{name}' created for ₹{target_amount:,.2f}")
    
    def update_savings_goal(self, goal_id: int, amount: float):
        """Add money to a savings goal"""
        for goal in self.data['savings_goals']:
            if goal['id'] == goal_id and goal['status'] == 'active':
                goal['current_amount'] += amount
                
                if goal['current_amount'] >= goal['target_amount']:
                    goal['status'] = 'completed'
                    print(f"\n🎉 Congratulations! Goal '{goal['name']}' completed!")
                else:
                    remaining = goal['target_amount'] - goal['current_amount']
                    percentage = (goal['current_amount'] / goal['target_amount'] * 100)
                    print(f"✓ ₹{amount:,.2f} added to '{goal['name']}'")
                    print(f"   Progress: {percentage:.1f}% | Remaining: ₹{remaining:,.2f}")
                
                self.save_data()
                return
        print("❌ Goal not found or already completed!")
    
    def view_savings_goals(self):
        """Display all savings goals with progress"""
        active_goals = [g for g in self.data['savings_goals'] if g['status'] == 'active']
        
        if not active_goals:
            print("\nNo active savings goals.")
            return
        
        print("\n" + "="*90)
        print("🎯 SAVINGS GOALS")
        print("="*90)
        
        for goal in active_goals:
            progress = (goal['current_amount'] / goal['target_amount'] * 100) if goal['target_amount'] > 0 else 0
            remaining = goal['target_amount'] - goal['current_amount']
            
            # Calculate days until deadline
            deadline_date = datetime.datetime.strptime(goal['deadline'], '%Y-%m-%d').date()
            days_left = (deadline_date - datetime.date.today()).days
            
            # Visual progress bar
            bar_length = 30
            filled = int(bar_length * min(progress / 100, 1))
            bar = "█" * filled + "░" * (bar_length - filled)
            
            priority_icon = {'high': '🔴', 'medium': '🟡', 'low': '🟢'}
            
            print(f"\n{priority_icon.get(goal['priority'], '⚪')} ID: {goal['id']} | {goal['name']}")
            print(f"   Target: ₹{goal['target_amount']:,.2f}")
            print(f"   Saved:  ₹{goal['current_amount']:,.2f} ({progress:.1f}%)")
            print(f"   [{bar}]")
            print(f"   Remaining: ₹{remaining:,.2f}")
            print(f"   Deadline: {goal['deadline']} ({days_left} days left)")
            
            # Calculate required monthly saving
            months_left = max(days_left / 30, 1)
            monthly_required = remaining / months_left
            print(f"   Required monthly saving: ₹{monthly_required:,.2f}")
        
        print("="*90)
    
    def expense_insights(self):
        """Provide intelligent insights on spending patterns"""
        print("\n" + "="*90)
        print("🔍 EXPENSE INSIGHTS & RECOMMENDATIONS")
        print("="*90)
        
        # Get last 3 months data
        insights = []
        current_date = datetime.date.today()
        
        # Analyze spending trends
        expense_by_month = defaultdict(float)
        for trans in self.data['transactions']:
            if trans['type'] == 'expense':
                month = trans['date'][:7]
                expense_by_month[month] += trans['amount']
        
        if len(expense_by_month) >= 2:
            months = sorted(expense_by_month.keys())
            if len(months) >= 2:
                current_month_spending = expense_by_month[months[-1]]
                previous_month_spending = expense_by_month[months[-2]]
                change = ((current_month_spending - previous_month_spending) / previous_month_spending * 100) if previous_month_spending > 0 else 0
                
                if change > 20:
                    insights.append(f"📈 Your spending increased by {change:.1f}% compared to last month. Review discretionary expenses!")
                elif change < -20:
                    insights.append(f"📉 Great job! Your spending decreased by {abs(change):.1f}% compared to last month.")
        
        # Identify highest spending category
        current_month = datetime.date.today().strftime('%Y-%m')
        category_spending = defaultdict(float)
        for trans in self.data['transactions']:
            if trans['type'] == 'expense' and trans['date'].startswith(current_month):
                category_spending[trans['category']] += trans['amount']
        
        if category_spending:
            top_category = max(category_spending.items(), key=lambda x: x[1])
            insights.append(f"💸 '{top_category[0]}' is your highest spending category this month: ₹{top_category[1]:,.2f}")
        
        # Check for recurring expenses
        recurring_expenses = [t for t in self.data['transactions'] 
                            if t['type'] == 'expense' and t['recurring']]
        if recurring_expenses:
            total_recurring = sum(t['amount'] for t in recurring_expenses 
                                if t['date'].startswith(current_month))
            insights.append(f"🔄 Recurring expenses total: ₹{total_recurring:,.2f} per month")
        
        # Savings goal progress check
        total_income, total_expense, _ = self.get_current_month_summary()
        if total_income > 0:
            current_savings = total_income - total_expense
            for goal in self.data['savings_goals']:
                if goal['status'] == 'active':
                    deadline_date = datetime.datetime.strptime(goal['deadline'], '%Y-%m-%d').date()
                    months_left = max((deadline_date - datetime.date.today()).days / 30, 1)
                    required_monthly = (goal['target_amount'] - goal['current_amount']) / months_left
                    
                    if current_savings < required_monthly:
                        insights.append(f"⚠️  To reach '{goal['name']}' goal, you need to save ₹{required_monthly:,.2f}/month. Current savings: ₹{current_savings:,.2f}")
        
        # Display insights
        if insights:
            for i, insight in enumerate(insights, 1):
                print(f"\n{i}. {insight}")
        else:
            print("\n✓ Keep tracking expenses to get personalized insights!")
        
        print("\n" + "="*90)
    
    def search_transactions(self, keyword: str):
        """Search transactions by keyword"""
        results = []
        keyword_lower = keyword.lower()
        
        for trans in self.data['transactions']:
            if (keyword_lower in trans['description'].lower() or
                keyword_lower in trans['category'].lower() or
                keyword_lower in ' '.join(trans['tags']).lower()):
                results.append(trans)
        
        if not results:
            print(f"\nNo transactions found matching '{keyword}'")
            return
        
        print(f"\n🔍 Search Results for '{keyword}' ({len(results)} found)")
        print("="*90)
        for trans in results:
            icon = "💰" if trans['type'] == 'income' else "💸"
            print(f"\n{icon} {trans['date']} | ₹{trans['amount']:,.2f} | {trans['category']}")
            print(f"   {trans['description']}")
        print("="*90)


def display_menu():
    """Display main menu"""
    print("\n" + "="*90)
    print("💼 PERSONAL FINANCE MANAGER & BUDGET TRACKER")
    print("="*90)
    print("\n💰 TRANSACTIONS")
    print("  1. Add Income")
    print("  2. Add Expense")
    print("  3. View All Transactions")
    print("  4. View Transactions (Filtered)")
    print("  5. Search Transactions")
    
    print("\n📊 BUDGETS & ANALYSIS")
    print("  6. Set Budget for Category")
    print("  7. View Budget Status")
    print("  8. Generate Monthly Report")
    print("  9. Expense Insights")
    
    print("\n🎯 SAVINGS & GOALS")
    print("  10. Add Savings Goal")
    print("  11. Update Savings Goal")
    print("  12. View Savings Goals")
    
    print("\n  13. Exit")
    print("-"*90)


def main():
    """Main application function"""
    manager = FinanceManager()
    
    print("\n" + "="*90)
    print("🎉 WELCOME TO PERSONAL FINANCE MANAGER!")
    print("="*90)
    """
    print("\n✨ Demo Mode: Sample transactions and budgets loaded!")
    print("💡 Tip: Try option 8 (Monthly Report) or 7 (Budget Status) first!")
    print("\nPre-loaded data includes:")
    print("  • 10 sample transactions (income & expenses)")
    print("  • 4 active budgets for different categories")
    print("  • 3 savings goals with progress tracking")
    print("  • 1 investment tracker entry")
    """
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-13): ").strip()
        
        if choice == '1':
            print("\n--- Add Income ---")
            try:
                amount = float(input("Amount (₹): "))
                print(f"Categories: {', '.join(manager.income_categories)}")
                category = input("Category: ").strip()
                description = input("Description: ").strip()
                payment_method = input("Payment Method (Bank Transfer/Cash/UPI/Others): ").strip()
                recurring = input("Recurring? (yes/no): ").strip().lower() == 'yes'
                tags = input("Tags (comma-separated, optional): ").strip()
                tag_list = [t.strip() for t in tags.split(',')] if tags else []
                manager.add_transaction('income', amount, category, description, 
                                      payment_method, recurring, tag_list)
            except ValueError:
                print("❌ Invalid amount!")
        
        elif choice == '2':
            print("\n--- Add Expense ---")
            try:
                amount = float(input("Amount (₹): "))
                print(f"Categories: {', '.join(manager.expense_categories)}")
                category = input("Category: ").strip()
                description = input("Description: ").strip()
                payment_method = input("Payment Method (Cash/Card/UPI/Others): ").strip()
                recurring = input("Recurring? (yes/no): ").strip().lower() == 'yes'
                tags = input("Tags (comma-separated, optional): ").strip()
                tag_list = [t.strip() for t in tags.split(',')] if tags else []
                manager.add_transaction('expense', amount, category, description,
                                      payment_method, recurring, tag_list)
            except ValueError:
                print("❌ Invalid amount!")
        
        elif choice == '3':
            manager.view_transactions()
        
        elif choice == '4':
            print("\nFilter by: income, expense")
            filter_type = input("Enter filter type (or 'all'): ").strip()
            month = input("Enter month (YYYY-MM) or press Enter for all: ").strip()
            manager.view_transactions(filter_type, month if month else None)
        
        elif choice == '5':
            keyword = input("Enter search keyword: ").strip()
            manager.search_transactions(keyword)
        
        elif choice == '6':
            print("\n--- Set Budget ---")
            print(f"Categories: {', '.join(manager.expense_categories)}")
            category = input("Category: ").strip()
            try:
                limit = float(input("Monthly Budget Limit (₹): "))
                threshold = int(input("Alert Threshold % (default 80): ") or "80")
                manager.set_budget(category, limit, threshold)
            except ValueError:
                print("❌ Invalid input!")
        
        elif choice == '7':
            manager.view_budget_status()
        
        elif choice == '8':
            manager.generate_monthly_report()
        
        elif choice == '9':
            manager.expense_insights()
        
        elif choice == '10':
            print("\n--- Add Savings Goal ---")
            name = input("Goal Name: ").strip()
            try:
                target = float(input("Target Amount (₹): "))
                deadline = input("Deadline (YYYY-MM-DD): ").strip()
                print("Priority: high, medium, low")
                priority = input("Priority: ").strip()
                manager.add_savings_goal(name, target, deadline, priority)
            except ValueError:
                print("❌ Invalid amount!")
        
        elif choice == '11':
            manager.view_savings_goals()
            try:
                goal_id = int(input("\nEnter Goal ID: "))
                amount = float(input("Amount to Add (₹): "))
                manager.update_savings_goal(goal_id, amount)
            except ValueError:
                print("❌ Invalid input!")
        
        elif choice == '12':
            manager.view_savings_goals()
        
        elif choice == '13':
            print("\n💰 Keep tracking your finances! Goodbye! 👋")
            break
        
        else:
            print("\n❌ Invalid choice! Please select 1-13.")
        
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()