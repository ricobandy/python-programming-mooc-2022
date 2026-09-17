# Write your solution here
str1 = input("Please type in the 1st word:")
str2 = input("Please type in the 2nd word:")
 
str1 = str1.lower()
str2 = str2.lower()
 
if str1 > str2:
    print(f"{str1} comes alphabetically last.")
elif str2 > str1:
    print(f"{str2} comes alphabetically last.")
else:
    print("You gave the same word twice.")