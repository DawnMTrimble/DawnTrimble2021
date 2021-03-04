'''
Tip Calculator will ask a user to enter the cost of their food, number of diners, and the percentage they would like to tip.\n
Calculator will add cost, tax and tip amount and divide by number of diners
'''

"""Roadmap\n  
User to input amount of the bill\n
amount of tax is a fixed variable\n
add the tax amount to the total bill\n
User to input percentage they would like to tip\n
User to input the number of people splitting the bill\n
Add food cost, tax and tip together and divide by number of people splitting the bill \n"""

#Declaring variables and input statements

food_cost = float(input("Please enter the cost of your bill:"))
tip_percent = float(input("How much would you like to tip?:"))
#check to make sure a decimal is entered
while tip_percent > 1:
    print("Invalid data. Please enter a decimal")
    tip_percent = float(input("How much would you like to tip?:"))

#encourage at least 20 percent for tip
if tip_percent < .20:
    print("Your server works off tips. Please consider a bigger tip.")
else:
    print("Thank you for your generosity!")

num_diners =  float(input("How many diners are splitting the tab?:"))
tax_amount = .10

#Calculate the tip amount

#The tip amount is the food cost multiplied by the tip percentage
tip_amount = food_cost * tip_percent
#The total amount of tax is the food cost * the total tax
total_tax = food_cost * tax_amount
#The total bill would be the total tax amount + the food cost + the tip amount
total_bill = total_tax + food_cost + tip_amount
#Per person total is the total_bill + the number of diners
per_person_total = total_bill/num_diners

#results
print(f"Your total with tax and tip is $ {total_bill}")
print(f"The amount each person should pay is $ {per_person_total}")