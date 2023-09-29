#Name: Benedict Waweru
#Registration number: SCT211-0032/2022

#This function adds two numbers
def add (x, y):
    return x + y

#This function subtracts two numbers
def subtract(x, y):
    return x - y

#This function multiplies two numbers
def multiply(x, y):
    return x * y

#This function divides two numbers
def divide(x, y):
    if y == 0:
        return "Division by zero is undefined!"
    return x / y

name = input("Please enter your name: ")
print("Welcome to my Calculator, " + name)

print("Select operation.")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")

while True:
    #Take input from the user
    choice = input("Enter choice (1/2/3/4/5): ")
    #Check if the choice is one of the five options
    if choice == '5':
        print("Exiting the calculator! Goodbye, " + name + "!")
        break
    if choice not in ('1', '2', '3', '4'):
        print("Invalid choice. Please select a valid operation.")
        continue

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))