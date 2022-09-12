"""
* Created By Miguel Gemio

* Date: 10/09/22
* time: 08:00
* Project Name: Lab 2 Exercise - Use arithmetic operators
"""

# TODO Calculate the distance between two planets

# Create variables to store the distances
first_planet, second_planet = 149597870, 778547200

# Subtract the values to determine the distance between teh planets.
distance_km = second_planet - first_planet
print(f"\nDistance in km: {distance_km}")

# Convert distance_km to miles by dividing it by 1.609344
distance_mi = distance_km / 1.609344
print(f"Distance in mi: {distance_mi}\n")
