# Write your solution here

count_of_numbers = 0
sum_of_numbers = 0
num_of_positives = 0
num_of_negatives = 0

print("Please type in integer numbers. Type in 0 to finish.")

while True:
    number = int(input("Number: "))

    if number == 0:
        break
    else:
        count_of_numbers = count_of_numbers + 1
        sum_of_numbers = sum_of_numbers + number
        if number > 0:
            num_of_positives = num_of_positives + 1
        if number < 0:
            num_of_negatives = num_of_negatives + 1

print("... the program asks for numbers")
print(f"Numbers typed in {count_of_numbers}")
print(f"The sum of the numbers is {sum_of_numbers}")
print(f"The mean of the numbers is {sum_of_numbers / count_of_numbers}")
print(f"Positive numbers {num_of_positives}")
print(f"Negative numbers {num_of_negatives}")