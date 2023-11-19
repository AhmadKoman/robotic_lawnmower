import os
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np
import math 
import random
import time

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

dt = 0.5



x0, y0 = find_start_cor(map)
print(f"({x0},{y0})")
vx,vy = get_velocity()
print(vx, vy)

def bounce(vx, vy):
    alpha = random.uniform(0, 2 * math.pi)
    new_vx = 0.3 * math.cos(alpha)
    new_vy = 0.3 * math.sin(alpha)
    return new_vx, new_vy

def one_step(x, y, vx, vy, dt):
    x_ny = x + (vx * dt)
    y_ny = y + (vy * dt)
    
    if not is_outside(x_ny, y_ny):
        x, y = x_ny, y_ny
        print(f"({x}, {y})")
    else:
        vx, vy = bounce(vx, vy)
    
    return x, y


time_limit = 15  # 10 minutes (adjust as needed)

# Load the map from the "simple.csv" file
current_directory = os.getcwd()
path = os.path.join(current_directory, "simple.csv")
map = read_csv_map(path)

# Determine the grid size for the coverage map
coverage_rows = len(map)
coverage_cols = len(map[0])

def update_coverage_map(coverage_map, x, y, prev_x, prev_y):
    if x != prev_x or y != prev_y:
        coverage_map[min(y, prev_y):max(y, prev_y) + 1, min(x, prev_x):max(x, prev_x) + 1] = 1

# Create the coverage map as a binary grid (0 or 1)
coverage_map = np.zeros((coverage_rows, coverage_cols), dtype=int)

# Get the start time
start_time = time.time()

x0, y0 = find_start_cor(map)
prev_x, prev_y = x0, y0

# ... (previous code)

# Continue until the time limit is reached or coverage is complete
while True:
    elapsed_time = time.time() - start_time

    if elapsed_time >= time_limit:
        break

    vx, vy = get_velocity()
    x0, y0 = one_step(x0, y0, vx, vy, dt)
    
    x_pixel, y_pixel = int(x0), int(y0)
    if 0 <= x_pixel < coverage_cols and 0 <= y_pixel < coverage_rows:
        update_coverage_map(coverage_map, x_pixel, y_pixel, prev_x, prev_y)
    
    prev_x, prev_y = x_pixel, y_pixel

    # Create the figure outside the loop or close it at the end of each iteration
    plt.figure()
    plt.imshow(coverage_map, cmap=ListedColormap(['white', 'blue']), origin='upper', aspect='equal')
    plt.title("Coverage Map")
    plt.pause(0.1)
    plt.close()  # Close the figure to prevent the "RuntimeWarning"

# ... (remaining code)


# Save the final coverage map as an image
plt.figure()
plt.imshow(coverage_map, cmap=ListedColormap(['white', 'blue']), origin='upper', aspect='equal')
plt.title("Final Coverage Map")
plt.savefig("final_coverage_map.png")
plt.show()
