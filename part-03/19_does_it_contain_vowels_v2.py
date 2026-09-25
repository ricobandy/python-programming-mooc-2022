# Write your solution here
input_str = input("Please type in a string: ")
vowels = "aeo"
index = 0

while index < len(vowels):
    if vowels[index] in input_str:
        print(f"{vowels[index]} found")
    else:
        print(f"{vowels[index]} not found")
    index += 1