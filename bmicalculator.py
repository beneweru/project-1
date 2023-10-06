# Name: Benedict Waweru
# Registration number: SCT211-0032/2022

# Input the height (in meters) and weight (in kilograms)
height = float(input("Enter your height (in meters): "))
weight = float(input("Enter your weight (in kilograms): "))

# Calculate BMI (Body Mass Index)
bmi = weight / (height ** 2)

# Determine the BMI category and provide feedback
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 24.9:
    category = "Normal Weight"
else:
    category = "Overweight"

# Display the BMI and category
print(f"Your BMI is: {bmi:.2f}")
print(f"You are categorized as: {category}")
