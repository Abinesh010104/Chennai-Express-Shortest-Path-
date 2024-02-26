import heapq


def dijkstra(graph, start):
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    predecessors = {}

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    return distances, predecessors


def shortest_path(graph, start, destination):
    distances, predecessors = dijkstra(graph, start)
    path = []
    current_node = destination
    while current_node != start:
        path.insert(0, current_node)
        current_node = predecessors[current_node]
    path.insert(0, start)
    return path
