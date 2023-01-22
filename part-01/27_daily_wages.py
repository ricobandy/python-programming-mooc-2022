# Write your solution here
hourly_wage = float(input("Hourly wage: "))
hours_worked = int(input("Hours worked: "))
work_day = input("Day of the week: ")
 
if work_day == "Sunday":
    print(f"Daily wages: {2 * hours_worked * hourly_wage} euros")
else:
    print(f"Daily wages: {hours_worked * hourly_wage} euros")