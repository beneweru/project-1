# Name: Benedict Waweru
# Registration number: SCT211-0032/2022

# The user inputs the total bill amount
total_bill = float(input("Enter the total bill amount: "))

# The user inputs the tip percentage either 10%, 12%, or 15%
while True:
    tip_percentage = input("Enter the tip percentage (10, 12, or 15): ")
    if tip_percentage in ["10", "12", "15"]:
        tip_percentage = int(tip_percentage)
        break
    else:
        print("Invalid tip percentage! Please enter 10, 12, or 15! ")

# This takes in input of number of people
number_of_people = int(input("Enter the number of people splitting the bill: "))

# This calculates the tip amount
tip_amount = (tip_percentage / 100) * total_bill

# This calculates the total amount to be paid
total_amount = total_bill + tip_amount

# This calculates the amount each person should pay
amount_per_person = total_amount / number_of_people

# This displays the result, rounded to two decimal points
print(f"Each person should pay: ${amount_per_person:.2f}")
