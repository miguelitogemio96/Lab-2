"""
* Created By Miguel Gemio

* Date: 10/09/22
* time: 08:00
* Project Name: Lab 2 Exercise - Convert strings to numbers and use 
*               absolute values
"""


# TODO Create an application to work with numbers and user input

"""
* We want to read the distance from the sun for two planets,
* then display the distance between the planets. 
* Do this by using input to read the values.
* Use int to convert to integer.
* Use abs to convert the result into its absolute value.
"""

first_planet_input = input('Enter the distance from the sun for the first '
                           'planet in KM: ')
second_planet_input = input('Enter the distance from the sun for the second '
                            'planet in KM: ')

# Convert to Numer
first_planet = int(first_planet_input)
second_planet = int(second_planet_input)

# Subtracting first_planet from second_planet and converting the result 
# to its absolute value by using abs.

distance_km = second_planet - first_planet
print(f'The distance is: {abs(distance_km)}')