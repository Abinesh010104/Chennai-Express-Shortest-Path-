import matplotlib.pyplot as plt


def plot_locations(coordinates, shortest_path_nodes):
    for location, (latitude, longitude) in coordinates.items():
        plt.plot(longitude, latitude, "bo")
        plt.text(longitude, latitude, location, fontsize=8)
    for i in range(len(shortest_path_nodes) - 1):
        start_coord = coordinates[shortest_path_nodes[i]]
        end_coord = coordinates[shortest_path_nodes[i + 1]]
        plt.plot([start_coord[1], end_coord[1]], [start_coord[0], end_coord[0]], "r-")

    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.title("Chennai Areas")
    plt.grid(True)
    plt.show()


def scale_coordinates(
    latitude, longitude, max_lat, min_lat, max_lon, min_lon, screen_width, screen_height
):
    scaled_x = (longitude - min_lon) / (max_lon - min_lon) * screen_width
    scaled_y = (latitude - min_lat) / (max_lat - min_lat) * screen_height
    return scaled_x, scaled_y
