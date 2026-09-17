# Write your solution here
gift_value = int(input("Value of gift: "))
tax_amt = 0
 
if gift_value < 5000:
    tax_amt = 0
elif gift_value >= 5000 and gift_value < 25000:
    tax_amt = 100 + (gift_value - 5000) * 0.08
elif gift_value >= 25000 and gift_value < 55000:
    tax_amt = 1700 + (gift_value - 25000) * 0.1
elif gift_value >= 55000 and gift_value < 200000:
    tax_amt = 4700 + (gift_value - 55000) * 0.12
elif gift_value >= 200000 and gift_value < 1000000:
    tax_amt = 22100 + (gift_value - 200000) * 0.15
elif gift_value >= 1000000:
    tax_amt = 142100 + (gift_value - 1000000) * 0.17
 
if tax_amt == 0:
    print("No tax!")
else:
    print(f"Amount of tax: {tax_amt} euros")  