import csv
import os

def read_ground_map(filename):
    ground_map = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            # Strip leading and trailing whitespace from each cell
            cleaned_row = [cell.strip() for cell in row]
            ground_map.append(cleaned_row)
    return ground_map

# Get the current working directory
current_directory = os.getcwd()

# Provide the relative path to the CSV file
filename = os.path.join(current_directory, "simple.csv")

hej = read_ground_map(filename)

# Define a color map
color_map = {
    'L': 'blue',
    'O': 'orange',
    'S': 'green'
}

import matplotlib.pyplot as plt

# Define a function to plot the colored grid
def plot_colored_map(ground_map, color_map):
    rows = len(ground_map)
    cols = len(ground_map[0])
    colored_map = []

    for row in ground_map:
        colored_row = [color_map[cell] for cell in row]
        colored_map.append(colored_row)

    plt.imshow(colored_map, interpolation='nearest')
    plt.show()

# Plot the colored map
plot_colored_map(hej, color_map)


