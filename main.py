import os
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np
import math 


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

x, y = find_start_cor(map)
print(f"({x},{y})")

x = [n/10 for n in range(0, 100)]
y = [math.sin(i) for i in x]
plt.plot(x, y)    # Deafult, lines connecting the dots
plt.show()

x = [n/4 for n in range(0, 40)]
y1 = [math.sin(i) for i in x]
y2 = [math.cos(i) for i in x]
plt.plot(x, y1, 'ro')      # ro ==> red circles
plt.plot(x, y2, 'b+')      # b+ ==> blue plus
plt.title('Sinus and cosinus')
plt.xlabel('x in range 0 to 10')
plt.ylabel('sin(x) as red, cos(x) as blue')
plt.show()


fig, (ax1, ax2) = plt.subplots(1, 2)  # Two plots called ax1 and ax2
x = [n for n in range(0, 20)]
y = [i**5 for i in x]

ax1.plot(x, y)
ax1.set_xlabel('n in range 0 to 20')
ax1.set_ylabel('n^5')
ax1.set_title('n vs n^5, non-logarithmic y-axis')
ax2.plot(x, y)
ax2.set_xlabel('n in range 0 to 20')
ax2.set_ylabel('n^5')
ax2.set_title('n vs n^5, logarithmic y-axis')
ax2.set_yscale('log')
plt.show()
