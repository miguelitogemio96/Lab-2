"""
* Created By Miguel Gemio

* Date: 10/09/22
* time: 12:00
* Project Name: Lab 2 Exercise - Format String

"""

# TODO Use variables that hold key facts about gravity on various moons 
#      and then use them to format and print the information.

# Creating three variables, name, gravity, and planet with their values
name, planet, gravity = "Ganymede", "Mars", 1.43

# Creating the template to display the information about the moon.
template = f"Gravity Facts about {name}\n\
------------------------------------\n\
Planet Name: {planet}\n\
Gravity on {name}: {gravity} m/s2"

print(template)

# Another option is:
template = f"""\nGravity Facts about {name} 
----------------------------------------
Planet Name: {planet}
Gravity on {name}: {gravity} m/s2"""

print(template)