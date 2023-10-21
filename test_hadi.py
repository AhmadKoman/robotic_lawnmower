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

filename = os.path.join(current_directory, "/simple/")

hej = read_ground_map(filename)
print(hej)
