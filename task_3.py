import heapq

def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        # Витягуємо вершину з найменшою відстанню
        current_distance, current_node = heapq.heappop(priority_queue)

        # Якщо знайдена відстань більша за збережену, продовжуємо
        if current_distance > distances[current_node]:
            continue

        # Перебираємо сусідів
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances

def create_graph():
    graph = {
        "A": {"B": 1, "C": 3},
        "B": {"A": 2, "C": 3, "D": 5},
        "C": {"A": 2, "B": 2, "D": 1},
        "D": {"B": 8, "C": 5},
    }
    return graph

def main():
    graph = create_graph()
    start = "A"
    distances = dijkstra(graph, start)
    
    for node, distance in distances.items():
        print(f"Відстань від {start} до {node}: {distance}")

if __name__ == "__main__":
    main()  