"""
* Created By Miguel Gemio

* Date: 11/09/22
* time: 10:00
* Project Name: Lab 2 Exercise - Boolean Logic in Python

"""

# Using complex logic to determine possible evasive maneuvers

# Code to the cell below to create two variables: object_size and proximity. 
# Set object_size to 10 to represent 10m3. Set proximity to 9000. Then add 
# the code to display a message saying Evasive maneuvers required if 
# both object_size is greater than 5 and proximity is less than 1000. 
# Otherwise display a message saying Object poses no threat.

object_size, proximity = 10, 9000


# I am usign a shortcurt of If and breaking the line with "\"
print('Evasive maneuvers required') if object_size > 5 and proximity < 1000 \
                                    else print('Object poses no threat')