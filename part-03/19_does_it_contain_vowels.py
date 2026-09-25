# Write your solution here
input_str = input("Please type in a string: ")
vowels = "aeo"

for letter in vowels:
    if letter in input_str:
        print(f"{letter} found")
    else:
        print(f"{letter} not found")