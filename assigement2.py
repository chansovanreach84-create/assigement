bill_input = input("Please enter the your total bill : $")
tip_input= input("Enter the percentage of tip that you wanna give :​%")

bill_amount = float(bill_input)
tip_percentage = float(tip_input)

tip_amount = (tip_percentage/100) * bill_amount
total_amount = bill_amount + tip_amount

print(f"Your total bill is : ${total_amount:.2f}")
print(f"Your tip amount is : ${tip_amount:.2f}")
print("Than you for supporting us !")