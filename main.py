import os
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


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
    rows = len(map)  # amount of rows in plot list
    cols = len(map[0])  # amount of coloms in plot list
    plt.figure()
    # Assign color to value: 0 = black, 1 = green, 2 = yellow, 3 = red
    col_map = ListedColormap(['black', 'green', 'yellow'], 'indexed')
    # Plot grid
    plt.pcolormesh(map, edgecolors='k', linewidth=2, cmap=col_map)
    # Fine tune plot layout
    ax = plt.gca()  # Get current axis object
    ax.set_yticks(range(0, rows+1, 1))
    ax.set_xticks(range(0, cols+1, 1))
    plt.title(f"Colored grid of size {rows}x{cols}")
    plt.show()
    return None


current_directory = os.getcwd()

path = os.path.join(current_directory, "simple.csv")

map = read_csv_map(path)
print(map)

visualize_map(map)
