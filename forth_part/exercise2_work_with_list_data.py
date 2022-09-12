"""
* Created By Miguel Gemio

* Date: 11/09/22
* time: 20:00
* Project Name: Lab 2 Exercise - Introduction to lists

"""

# Use slices to retrieve portions of a list

# List of planets
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Neptune"]

# Read the name of a planet (capitalize)
user_planet = input("Please enter the name of the planet: ").capitalize()

# Get the index of the planet
planet_index = planets.index(user_planet)

# Print the results
print(f"Here are the planets closer than {user_planet}\n-->", 
      *planets[0:planet_index])

# Display planets further
print(f"Here are the planets further than {user_planet}\n-->", 
      *planets[planet_index + 1:])