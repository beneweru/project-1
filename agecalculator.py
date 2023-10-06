# Name: Benedict Waweru
# Registration number: SCT211-0032/2022

from datetime import datetime

# The user inputs their year of birth as an integer
year_of_birth = int(input("Enter your birth year: "))

# Get the current date
current_date = datetime.now()

# Calculate the age
age = current_date.year - year_of_birth

# Calculate months and days
birth_date = datetime(year_of_birth, current_date.month, current_date.day)
if current_date < birth_date:
    age -= 1 # Subtract 1 year if the birth date hasn't occurred yet

months = (current_date.year - birth_date.year) * 12 + (current_date.month - birth_date.month)
days = (current_date - birth_date).days

# Display the age as output
print(f"Your age is {age} years, {months} months, and {days} days.")