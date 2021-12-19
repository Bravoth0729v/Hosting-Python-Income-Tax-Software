income = int(input("Enter Your Income Yearly: "))
tax = 0
cess = 0
if income <= 250000:
    tax = 0
    # print("Your Tax is: ",tax)
elif income <= 500000:
    tax = (income - 250000)*0.05
    # print("Your Tax is: ",tax)
elif income <= 1000000:
    tax = 12500 + (income -  500000 )*0.2
    # print("Your Tax is: ",tax)
else:
    tax = 12500 + 100000 + (income - 1000000 )*0.3
    # print("Your Tax is: ",tax)
cess = tax*0.04
ttax = tax + cess
print("Income Tax is: ",tax)
print("Health and education cess is: ",cess)
print("Your Total Tax is: ",ttax)