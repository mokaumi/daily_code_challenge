import datetime

def display_menu():
    print("\n=== EXPENSE TRACKER ===")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Exit")

def add_expense(expenses):
    name = input("Enter expense name: ")
    try:
        amount = float(input("Enter amount: ₦"))
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        expenses.append({"name": name, "amount": amount, "date": date})
        print(f"✅ Expense '{name}' added!")
    except ValueError:
        print("❌ Please enter a valid amount!")

def view_expenses(expenses):
    if not expenses:
        print("⚠️ No expenses recorded yet.")
    else:
        print("\nYour Expenses:")
        for idx, expense in enumerate(expenses, start=1):
            print(f"{idx}. {expense['name']} - ₦{expense['amount']} on {expense['date']}")

def total_expenses(expenses):
    total = sum(expense["amount"] for expense in expenses)
    print(f"💵 Total Expenses: ₦{total}")

def main():
    expenses = []

    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            total_expenses(expenses)
        elif choice == '4':
            print("👋 Exiting Expense Tracker. See you later!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
