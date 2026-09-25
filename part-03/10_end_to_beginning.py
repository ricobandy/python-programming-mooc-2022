# Write your solution here
input_string = input("Please type in a string: ")
string_size = len(input_string)

while string_size > 0:
    print(input_string[string_size - 1])
    string_size -= 1