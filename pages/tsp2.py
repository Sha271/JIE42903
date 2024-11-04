import matplotlib.pyplot as plt
from itertools import permutations, combinations
from random import shuffle
import random
import numpy as np
import statistics
import pandas as pd
import seaborn as sns
import streamlit as st

# Interactive Python Code for Coordinate and City Name Input

# Exercise: Adding Coordinates and City Names
print("Exercise: Coordinate and City Name Input")

# Initialize an empty dictionary to store city names with their coordinates
city_coordinates = {}

# Instructions
print("You'll be prompted to enter coordinates (x, y) and a city name.")
print("Enter 'done' as the city name when you've finished adding entries.\n")

# Collecting coordinate and city name information from the user
while True:
    city_name = input("Enter city name (or type 'done' to finish): ")
    if city_name.lower() == 'done':
        break
    try:
        x = float(input(f"Enter x-coordinate for {city_name}: "))
        y = float(input(f"Enter y-coordinate for {city_name}: "))
        city_coordinates[city_name] = (x, y)
        print(f"Added {city_name} with coordinates ({x}, {y}).\n")
    except ValueError:
        print("Invalid input. Please enter numeric values for coordinates.")

# Display the final dictionary of cities with coordinates
print("\nFinal list of city coordinates:")
for city, coords in city_coordinates.items():
    print(f"{city}: Coordinates {coords}")
print("\n")

# Additional Functionality (Optional):
# Prompt to update a city's coordinates
update_city = input("Would you like to update coordinates for a city? Enter city name or 'no': ")
if update_city in city_coordinates:
    try:
        new_x = float(input(f"Enter new x-coordinate for {update_city}: "))
        new_y = float(input(f"Enter new y-coordinate for {update_city}: "))
        city_coordinates[update_city] = (new_x, new_y)
        print(f"Updated {update_city} coordinates to ({new_x}, {new_y}).")
    except ValueError:
        print("Invalid input. Update failed.")
elif update_city.lower() != 'no':
    print(f"City {update_city} not found.")

# Final display of updated dictionary
print("\nUpdated city coordinates:")
for city, coords in city_coordinates.items():
    print(f"{city}: Coordinates {coords}")
