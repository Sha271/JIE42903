import matplotlib.pyplot as plt
from itertools import permutations, combinations
from random import shuffle
import random
import numpy as np
import statistics
import pandas as pd
import seaborn as sns
import streamlit as st

# Collect city names and their coordinates from user input
#cities_names = []
#x = []
#y = []

x = [0,3,6,7,15,10,16,5,8,1.5]
y = [1,2,1,4.5,-1,2.5,11,6,9,12]
cities_names = ["Gliwice", "Cairo", "Rome", "Krakow", "Paris", "Alexandria", "Berlin", "Tokyo", "Rio", "Budapest"]
city_coords = dict(zip(cities_names, zip(x, y)))
n_population = 250
crossover_per = 0.8
mutation_per = 0.2
n_generations = 200

print("Enter city names and their coordinates. Type 'done' to finish.")

while True:
    city_name = input("Enter city name (or 'done' to finish): ")
    if city_name.lower() == 'done':
        break
    try:
        x_coord = float(input(f"Enter x-coordinate for {city_name}: "))
        y_coord = float(input(f"Enter y-coordinate for {city_name}: "))
        cities_names.append(city_name)
        x.append(x_coord)
        y.append(y_coord)
        print(f"Added {city_name} at ({x_coord}, {y_coord})")
    except ValueError:
        print("Invalid input. Please enter numeric values for coordinates.")

# Create the city coordinates dictionary
city_coords = dict(zip(cities_names, zip(x, y)))

# Sample settings for other parameters
n_population = 250
crossover_per = 0.8
mutation_per = 0.2
n_generations = 200

# Pastel Palette for plotting
colors = sns.color_palette("pastel", len(cities_names))

# City Icons (adjust as needed if you have fewer/more cities)
city_icons = {
    "Gliwice": "♕", "Cairo": "♖", "Rome": "♗", "Krakow": "♘",
    "Paris": "♙", "Alexandria": "♔", "Berlin": "♚", "Tokyo": "♛",
    "Rio": "♜", "Budapest": "♝"
}

# Your existing plotting code and genetic algorithm functions go here

# Example of using the collected data for plotting
fig, ax = plt.subplots()

for i, (city, (city_x, city_y)) in enumerate(city_coords.items()):
    color = colors[i % len(colors)]
    icon = city_icons.get(city, "●")  # Use ● if no icon is defined for the city
    ax.scatter(city_x, city_y, c=[color], s=1200, zorder=2)
    ax.annotate(icon, (city_x, city_y), fontsize=40, ha='center', va='center', zorder=3)
    ax.annotate(city, (city_x, city_y), fontsize=12, ha='center', va='bottom', xytext=(0, -30), textcoords='offset points')

# Rest of the code (e.g., connecting cities and displaying plot in Streamlit) continues here...
st.pyplot(fig)
