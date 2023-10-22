import os
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np
import math 
import random


def read_csv_map(path):
    plot_map_list = []
    with open(path, "r") as file:
        for line in file:
            row = []
            for a in line.strip().split(","):
                if a == "L":
                    row.append(1)
                elif a == "O":
                    row.append(0)
                else:
                    row.append(2)
            plot_map_list.append(row)
    plot_map_list.reverse()
    return plot_map_list


def is_outside(x, y):
    global map
    if 0 <= x <= len(map[0]) and 0 <= y <= len(map):
        if map[int(y)][int(x)] == 0:
            return True
        return False
    return True



def visualize_map(map):
    rows = len(map)
    cols = len(map[0])

    map_array = np.array(map)  # Convert the map list to a NumPy array

    plt.figure()
    col_map = ListedColormap(['black', 'green', 'yellow'], 'indexed')
    plt.pcolormesh(map_array, edgecolors='k', linewidth=2, cmap=col_map)
    ax = plt.gca()
    ax.set_yticks(range(0, rows+1, 1))
    ax.set_xticks(range(0, cols+1, 1))
    plt.title(f"Colored grid of size {rows}x{cols}")
    plt.show()


current_directory = os.getcwd()

path = os.path.join(current_directory, "simple.csv")

map = read_csv_map(path)
print(map)

visualize_map(map)
plt.savefig('map.png')  # Save the plot to a file
plt.show()  # Display the plot

def find_start_cor(map):
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == 2:
                return x, y  # Return the x and y coordinates
            
def get_velocity():
    v = 0.3
    alpha = random.uniform(0, 2 * math.pi)
    vx = v * math.cos(alpha)
    vy = v * math.sin(alpha)
    return vx, vy

x0, y0 = find_start_cor(map)
print(f"({x0},{y0})")
vx,vy=get_velocity()
print(vx, vy)



