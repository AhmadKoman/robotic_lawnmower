import csv
import os

def read_ground_map(filename):
    ground_map = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            ground_map.append(row)
    return ground_map

current_directory = os.getcwd()

filename = os.path.join(current_directory, "simple.csv")

map = read_ground_map(filename)
print(map)

color_map = {'L': 'blue',  'O': 'orange', 'S': 'green'}


import matplotlib.pyplot as plt


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
plot_colored_map(map, color_map)