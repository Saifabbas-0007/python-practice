#input we need from the user
#total rent
#total ordered for snacks
#telectricity unit spend
#charge per unit
#person living in flat

#output
#total amount you have to pay!!

rent = int(input("enter your flat rent = "))
food = int(input("enter the amount of food order = "))
electricity_bill = int(input("enter total electricity spend = "))
charge_per_unit = int(input("enter the charge per unit = "))
persons = int(input("enter the number of person living in the flat = "))

total_bills = electricity_bill * charge_per_unit

output = (rent + food + total_bills) // persons

print("Each person will pay", output)
