import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, description, category):
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError("Amount must be greater than zero.")
        except ValueError:
            print("Invalid amount. Please enter a valid number.")
            return
        
        expense = {
            'date': datetime.datetime.now(),
            'amount': amount,
            'description': description,
            'category': category
        }
        self.expenses.append(expense)
        print("Expense added successfully.")

    def view_monthly_summary(self, month, year):
        total_expenses = 0
        for expense in self.expenses:
            if expense['date'].month == month and expense['date'].year == year:
                total_expenses += expense['amount']
        
        print(f"Total expenses for {datetime.date(year, month, 1).strftime('%B %Y')}: ${total_expenses:.2f}")

    def view_category_summary(self, category):
        total_expenses = 0
        for expense in self.expenses:
            if expense['category'].lower() == category.lower():
                total_expenses += expense['amount']
        
        print(f"Total expenses for {category}: ${total_expenses:.2f}")

# Example usage
if __name__ == "__main__":
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Monthly Summary")
        print("3. View Category-wise Summary")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            amount = input("Enter amount spent: ")
            description = input("Enter description: ")
            category = input("Enter category: ")
            tracker.add_expense(amount, description, category)
        
        elif choice == '2':
            month = int(input("Enter month (1-12): "))
            year = int(input("Enter year: "))
            tracker.view_monthly_summary(month, year)

        elif choice == '3':
            category = input("Enter category: ")
            tracker.view_category_summary(category)

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
