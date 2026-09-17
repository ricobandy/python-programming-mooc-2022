# Write your solution here
char1 = input("1st letter: ")
char2 = input("2nd letter: ")
char3 = input("3rd letter: ")
 
middle = ""
 
if char1 < char2 and char1 < char3:
    if char2 < char3:
        middle = char2
    else:
        middle = char3
elif char2 < char1 and char2 < char3:
    if char1 < char3:
        middle = char1
    else:
        middle = char3
elif char3 < char1 and char3 < char2:
    if char1 < char2:
        middle = char1
    else:
        middle = char2
 
print(f"The letter in the middle is {middle}")