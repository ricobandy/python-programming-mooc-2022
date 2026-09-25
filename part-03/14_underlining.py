# Write your solution here

while True:
    string = input("Please type in a string: ")
    size = len(string)

    if string == "":
        break

    print(string)
    print("-" * size)