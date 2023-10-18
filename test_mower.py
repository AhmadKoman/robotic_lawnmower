import random
import matplotlib.pyplot as plt
import numpy as np

# Define ground map (example)
ground_map = np.array([
    ['L', 'L', 'O', 'L', 'L'],
    ['L', 'L', 'O', 'L', 'L'],
    ['L', 'L', 'L', 'L', 'L'],
    ['L', 'L', 'L', 'S', 'L'],
])

# Define constants
v = 0.3  # Robot speed (m/s)
dt = 1.0  # Time step (seconds)
N = 5  # Grid division for coverage
simulation_duration = 3600  # Extended duration in seconds (60 minutes)

# Define symbols
LAWN = 'L'
OBSTACLE = 'O'
START = 'S'

# Get the shape of the ground map
rows, cols = ground_map.shape

# Initialize robot position
x, y = np.where(ground_map == START)
x, y = float(x), float(y)
vx, vy = 0.0, 0.0

# Create a coverage map
coverage_map = np.zeros((rows * N, cols * N))

# Simulate robot movement with a preference for unvisited areas
trace = []
current_time = 0
while current_time < simulation_duration:
    # Calculate the preference for unvisited directions
    preferences = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    random.shuffle(preferences, random=random.random)

    for preference in preferences:
        new_x = x + preference[0]
        new_y = y + preference[1]

        # Check if the new position is within the map and unvisited
        if 0 <= new_x < rows and 0 <= new_y < cols and coverage_map[int(new_x * N), int(new_y * N)] == 0:
            x = new_x
            y = new_y
            break

    trace.append((x, y))
    current_time += dt

# Mark visited pixels in the coverage map
for x, y in trace:
    i, j = int(x * N), int(y * N)
    if 0 <= i < rows * N and 0 <= j < cols * N:
        coverage_map[i, j] = 1

# Calculate coverage percentage
visited_pixels = np.sum(coverage_map)
total_pixels = rows * N * cols * N
coverage_percentage = (visited_pixels / total_pixels) * 100

print(f"Coverage: {coverage_percentage:.2f}%")
print(f"Time Duration: {simulation_duration} seconds")

# Visualize coverage map
plt.imshow(coverage_map, cmap='Blues', interpolation='none', origin='lower')
plt.title('Coverage Map')
plt.colorbar()
plt.show()
