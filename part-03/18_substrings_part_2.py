# Write your solution here

string = input("Please type in a string: ")
size = len(string)

count = size - 1

while count >= 0:
    print(string[count:])
    count  -= 1