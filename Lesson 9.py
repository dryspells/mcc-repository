income = 0
def main():
    print("Welcome to the monthly budget calculator!") 

def calculate_income():
    while True:
        user_input = input("Please enter your monthly income (must be greater than 0): ")
        try:
            income = float(user_input)
            if income <= 0:
                print("Invalid input. Please enter a positive number.")
                continue
            else:
                return income
        except ValueError:
            print("Invalid input. Please enter a number greater than 0.")

def obtain_expenses():
    expenses = []
    while True:
        amount_input = input("Enter an expense amount (or type 'done' to finish): ")
        if amount_input.lower() == 'done':
            break
        try:
            amount = float(amount_input)
            if amount < 0:
                print("Invalid input. Please enter a non-negative number.")
                continue
            expenses.append(amount)
        except ValueError:
            print("Invalid input. Please enter a number or 'done'.")
    return expenses

def calculate_budget(income, expenses):
    total_expenses = sum(expenses)
    remaining_budget = income - total_expenses
    return total_expenses, remaining_budget

def display_budget():
    income = calculate_income()
    expenses = obtain_expenses()
    total_expenses, remaining_budget = calculate_budget(income, expenses)
    print("\nBudget Summary:")
    print(f"Total Income: ${income:,.2f}")
    print(f"Total Expenses: ${total_expenses:,.2f}")
    print(f"Remaining Budget: ${remaining_budget:,.2f}")
    print(f"Expenses List: {expenses}")
    print("Thank you for using the monthly budget calculator!")
    print("Goodbye!")
    print("Completed by, Gregary Coplan")



if __name__ == "__main__":
    main()
    display_budget()
