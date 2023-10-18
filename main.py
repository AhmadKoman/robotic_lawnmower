import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import os
import math
import random
def plot_map(rows, cols):
    path = "/simple.csv"
    with open (path , "r", encoding="utf-8") as file:
        plot_map.reverse()
        rows = len(plot_map)
        cols = len(plot_map[0])