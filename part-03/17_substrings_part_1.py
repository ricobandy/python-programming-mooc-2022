# Write your solution here
string = input("Please type in a string: ")
size = len(string)

count = 1

while count <= size:
    print(string[0:count])
    count += 1