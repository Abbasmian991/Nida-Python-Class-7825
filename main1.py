#=====RENT CALCULATOR=======#
# input we need from the user
# Total food ordered for snacking
# Electricity units spent
# Charge per unit
# Persons living in room/flat
# Output
# Total amount you've to pay is

# rent = int (input("Enter your flat rent ="))
# food = int (input("Enter the amount of food ordered ="))
# electricity_spent = int (input("Enter the total of electricity spent ="))
# charge_per_unit = int (input("Enter the charge per unit ="))
# persons = int (input("Enter the number of persons living in room/flat ="))

# total_bill = electricity_spent * charge_per_unit

# output = (rent + food + total_bill)  // persons

# print("Each person will pay = ", output)

rent = float (input("Enter your flat rent ="))
food = float (input("Enter the amount of food ordered ="))
electricity_spent = float (input("Enter the total of electricity spent ="))
charge_per_unit = float (input("Enter the charge per unit ="))
persons = float (input("Enter the number of persons living in room/flat ="))

total_bill = electricity_spent * charge_per_unit

output = (rent + food + total_bill)  // persons

print("Each person will pay = ", output)