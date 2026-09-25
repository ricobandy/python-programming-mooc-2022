# Write your solution here
limit = int(input("Limit: "))
sum = 0
number = 1

while sum < limit:
    sum = sum + number
    number += 1

print(sum)