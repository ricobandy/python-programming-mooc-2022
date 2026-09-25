# Write your solution here

limit = int(input("Limit: "))
sum = 0
number = 1
statement =""

while sum < limit:
    sum = sum + number
    statement += str(number)
    number += 1

final_statement = " + ".join(statement)
print(f"The consecutive sum: {final_statement} = {sum}")

# model solution

limit = int(input("Limit: "))
number = 1
sum = 1
numbers = "1"
while sum < limit:
    number += 1
    sum += number
    # note that f-string can also be used like this
    numbers += f" + {number}"
print(f"The consecutive sum: {numbers} = {sum}")