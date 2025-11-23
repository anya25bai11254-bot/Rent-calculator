rent = int(input("Enter your hostel/flat rent = "))
food = int(input("Enter your amount of food ordered = "))
electricity_spend = int(input("Enter the total of electricity spend = "))
charge_per_unit = int(input("Enter the charge per unit = "))
persons = int(input("Enter the number of persons living in room/flat = "))

Total_Bill = electricity_spend * charge_per_unit

output = (food + rent + Total_Bill) // persons

print("Each person will pay = ", output )
