import csv

def read_ground_map(filename):
    ground_map = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            ground_map.append(row)
    return ground_map


import matplotlib.pyplot as plt

def visualize_ground_map(ground_map):
    # Implement code to visualize the ground map using Matplotlib.
    # You can use 'imshow' or 'pcolor' to create a grid-based representation.
    # Add labels for L (lawn), O (obstacle), and S (start point).
    plt.show()


def simulate_lawnmower_movement(ground_map, v, dt):
    # Implement the logic for simulating lawnmower movement.
    # Keep track of position (x, y) and use random bouncing when obstacles are encountered.
    # Record the positions over time to create the trace.
    trace = [(x_start, y_start)]  # Initialize trace with the starting point.
    return trace


def calculate_coverage(ground_map, trace, N):
    # Divide the ground map into smaller grid cells (pixels) with size N x N.
    # Track which cells have been visited by the lawnmower during the simulation.
    visited_pixels = [[0] * len(ground_map[0]) for _ in range(len(ground_map))]
    # Compute the percentage of visited cells based on the total number of cells.
    coverage_percentage = (sum(map(sum, visited_pixels)) / (len(ground_map) * len(ground_map[0]))) * 100
    return coverage_percentage



def visualize_coverage_map(visited_pixels):
    # Implement code to visualize the coverage map using Matplotlib.
    # Use colors to distinguish visited and unvisited cells.
    plt.imshow(visited_pixels, cmap='viridis', interpolation='nearest')
    plt.colorbar()
    plt.show()


def multiple_simulations(ground_map, v, dt, N, num_simulations, simulation_duration):
    # Run multiple simulations and store coverage results for analysis.
    coverage_results = []
    for _ in range(num_simulations):
        trace = simulate_lawnmower_movement(ground_map, v, dt)
        coverage = calculate_coverage(ground_map, trace, N)
        coverage_results.append(coverage)
    # Calculate average and standard deviation of coverage.
    average_coverage = sum(coverage_results) / len(coverage_results)
    std_deviation = statistics.stdev(coverage_results)
    return average_coverage, std_deviation


import random
import math

def generate_random_angle():
    return random.uniform(0, 2 * math.pi)


def is_obstacle(ground_map, x, y):
    # Check if the current position (x, y) is on an obstacle or outside the map.
    if x < 0 or x >= len(ground_map) or y < 0 or y >= len(ground_map[0]):
        return True
    return ground_map[int(x)][int(y)] == 'O'


def elastic_collision(vx, vy, normal_angle):
    # Implement an elastic collision for bouncing off obstacles.
    angle_diff = 2 * normal_angle - math.atan2(vy, vx)
    new_vx = v * math.cos(angle_diff)
    new_vy = v * math.sin(angle_diff)
    return new_vx, new_vy


import time

def simulate_grass_growth(ground_map, growth_schedule):
    # Simulate grass growth over time based on a predefined schedule.
    for day, schedule in enumerate(growth_schedule):
        if day % 7 == 0:  # Weekly schedule
            for x, y in schedule:
                ground_map[x][y] = 'L'  # Set cells to grass
        time.sleep(1)  # Simulate time passage (you can adjust the delay)


import matplotlib.pyplot as plt

def sensitivity_analysis(ground_map, v_values, dt_values, N_values):
    results = []

    for v in v_values:
        for dt in dt_values:
            for N in N_values:
                trace = simulate_lawnmower_movement(ground_map, v, dt)
                coverage = calculate_coverage(ground_map, trace, N)
                results.append((v, dt, N, coverage))

    return results


def plot_sensitivity_results(results):
    # Plot sensitivity analysis results (e.g., using 3D or contour plots).
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    v_values, dt_values, N_values, coverage_values = zip(*results)
    ax.scatter(v_values, dt_values, N_values, c=coverage_values, cmap='viridis')
    ax.set_xlabel('Velocity (v)')
    ax.set_ylabel('Time Step (dt)')
    ax.set_zlabel('Grid Size (N)')
    ax.set_title('Sensitivity Analysis')
    plt.show()


