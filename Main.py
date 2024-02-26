import turtle
from ShortestPath import shortest_path
from PlotLocation import scale_coordinates, plot_locations
from Data import dist, coordinates

print("Chennai Express : Shortest Path")
source_node = input("Enter Source :").lower().capitalize()
destination_node = input("Enter Destination :").lower().capitalize()
shortest_path_nodes = shortest_path(dist, source_node, destination_node)
plot_locations(coordinates, shortest_path_nodes)
