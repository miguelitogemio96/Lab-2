"""
* Created By Miguel Gemio

* Date: 11/09/22
* time: 19:00
* Project Name: Exercise - Age Calculator
"""

# Create a simple program that reads your age and calculates how old you are 
# in decades



# * Ask the user for input and validate the number
while True:
    age = input("Type your Age: ")
    try:
        age = int(age)  # Convert to integer
        if age > 0:
            break
        else:
            print("Incorrect data, please enter a number > 0")
    except ValueError:
        print("Incorrect data, please enter a number")
        
# * Calculate the decades and years
decades, years = age//10, age%10

# * Print result to screen
print(f"Your age in decades: {decades} and years: {years}")

 

