# Write your solution here
num_of_eating = int(input("How many times a week do you eat at the student cafeteria? "))
price_per_lunch = float(input("The price of a typical student lunch? "))
amt_of_groceries = float(input("How much money do you spend on groceries in a week? "))
weekly_expense = amt_of_groceries + (num_of_eating * price_per_lunch)
daily_expense = weekly_expense / 7
print()

print("Average food expenditure:")
print(f"Daily: {daily_expense} euros")
print(f"Weekly: {weekly_expense} euros")