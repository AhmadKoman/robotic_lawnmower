

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

