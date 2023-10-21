import os
import csv
import numpy as np
def plot_map(rows, cols):
    path = "/simple.csv"
    with open (path , "r", encoding="utf-8") as file:
        plot_map.reverse()
        rows = len(plot_map)
        cols = len(plot_map[0])
    
    rows, cols = plot_map.shape
    N = 10
    cov = np.zeros((rows * N, cols * N))
    