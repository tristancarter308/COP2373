#Tristan Carter 09/27/2025
#This program will ask users for an expense type and amount for the month and will return the total, highest,
#and lowest monthly expense.

from functools import reduce

#Ask user for monthly expense type and amount.
def get_expenses():
    expenses = []
    while True:
        expense_type = input("Enter expense type, when you are finished enter 'x': ").strip()
        if expense_type.lower() == 'x':
            break
        try:
            amount = float(input(f"Amount for {expense_type}: $"))
            expenses.append({'type': expense_type, 'amount': amount})
        except ValueError:
            print("Invalid. Please enter a number.")
    return expenses


#Find monthly total, highest, and lowest
def analyze_expenses(expenses):

    # Calculate total expense
    total_expense = reduce(lambda acc, expense: acc + expense['amount'], expenses, 0)

    # Find highest expense
    highest_expense = reduce(lambda acc, expense: expense if expense['amount'] > acc['amount'] else acc, expenses)

    # Find lowest expense
    lowest_expense = reduce(lambda acc, expense: expense if expense['amount'] < acc['amount'] else acc, expenses)

    return total_expense, highest_expense, lowest_expense

#Main function to run expense tracker
def main():
    monthly_expenses = get_expenses()

    #Display monthly total, highest, and lowest expenses.
    total, highest, lowest = analyze_expenses(monthly_expenses)
    print(f"\nTotal monthly expenses: ${total:.2f}")
    print(f"Highest expense: {highest['type']}  ${highest['amount']:.2f}")
    print(f"Lowest expense: {lowest['type']}  ${lowest['amount']:.2f}")


if __name__ == "__main__":
    main()