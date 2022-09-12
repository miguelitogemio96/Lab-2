"""
* Created By Miguel Gemio

* Date: 11/09/22
* time: 10:00
* Project Name: Lab 2 Exercise - Introduction to lists

"""

# Create and use Python lists to show information about the planets.
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus",
           "Neptune", "Pluto"]

print(*planets)


# Total number of planets by using len.
print(f"There are {len(planets)} planets.\n")

# Delete Jupiter of the list
planets.remove("Jupiter")

print("Actually, there are", len(planets), "planets")
print(*planets)
print(planets[-1], "is the last planet")