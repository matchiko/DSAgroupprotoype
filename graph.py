from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def add_vertex(self, station):
        self.graph[station] = []

    def add_edge(self, station1, station2):
        self.graph[station1].append(station2)
        self.graph[station2].append(station1)

def build_mrt_lrt_graph():
    # Create a graph representing MRT and LRT lines in the Philippines
    mrt_lrt_graph = Graph()
    
    mrt_lrt_graph.add_vertex('North Avenue')
    mrt_lrt_graph.add_vertex('Quezon Avenue')
    mrt_lrt_graph.add_vertex('Kamuning')
    mrt_lrt_graph.add_vertex('MRT Cubao')
    mrt_lrt_graph.add_vertex('MRT Santolan')
    mrt_lrt_graph.add_vertex('Ortigas')
    mrt_lrt_graph.add_vertex('Shaw Boulevard')
    mrt_lrt_graph.add_vertex('Boni')
    mrt_lrt_graph.add_vertex('Guadalupe')
    mrt_lrt_graph.add_vertex('Buendia')
    mrt_lrt_graph.add_vertex('Ayala')
    mrt_lrt_graph.add_vertex('Magallanes')
    mrt_lrt_graph.add_vertex('Taft Avenue')
    mrt_lrt_graph.add_vertex('Baclaran')
    mrt_lrt_graph.add_vertex('EDSA')
    mrt_lrt_graph.add_vertex('Libertad')
    mrt_lrt_graph.add_vertex('Gil Puyat')
    mrt_lrt_graph.add_vertex('Vito Cruz')
    mrt_lrt_graph.add_vertex('Quirino')
    mrt_lrt_graph.add_vertex('Pedro Gil')
    mrt_lrt_graph.add_vertex('United Nations')
    mrt_lrt_graph.add_vertex('Central Terminal')
    mrt_lrt_graph.add_vertex('Carriedo')
    mrt_lrt_graph.add_vertex('Doroteo Jose')
    mrt_lrt_graph.add_vertex('Bambang')
    mrt_lrt_graph.add_vertex('Tayuman')
    mrt_lrt_graph.add_vertex('Recto')
    mrt_lrt_graph.add_vertex('Legarda')
    mrt_lrt_graph.add_vertex('Pureza')
    mrt_lrt_graph.add_vertex('V. Mapa')
    mrt_lrt_graph.add_vertex('J. Ruiz')
    mrt_lrt_graph.add_vertex('Gilmore')
    mrt_lrt_graph.add_vertex('Betty Go-Belmonte')
    mrt_lrt_graph.add_vertex('Araneta Center-Cubao')
    mrt_lrt_graph.add_vertex('Anonas')
    mrt_lrt_graph.add_vertex('Katipunan')
    mrt_lrt_graph.add_vertex('LRT Santolan')
    mrt_lrt_graph.add_vertex('Marikina')
    mrt_lrt_graph.add_vertex('Antipolo')

  # MRT Line 3
    mrt_lrt_graph.add_edge('North Avenue', 'Quezon Avenue')
    mrt_lrt_graph.add_edge('Quezon Avenue', 'Kamuning')
    mrt_lrt_graph.add_edge('Kamuning', 'MRT Cubao')
    mrt_lrt_graph.add_edge('MRT Cubao', 'MRT Santolan')
    mrt_lrt_graph.add_edge('MRT Santolan', 'Ortigas')
    mrt_lrt_graph.add_edge('Ortigas', 'Shaw Boulevard')
    mrt_lrt_graph.add_edge('Shaw Boulevard', 'Boni')
    mrt_lrt_graph.add_edge('Boni', 'Guadalupe')
    mrt_lrt_graph.add_edge('Guadalupe', 'Buendia')
    mrt_lrt_graph.add_edge('Buendia', 'Ayala')
    mrt_lrt_graph.add_edge('Ayala', 'Magallanes')
    mrt_lrt_graph.add_edge('Magallanes', 'Taft Avenue')

    # MRT to LRT Line 2 (interchange at Araneta Center-Cubao)
    mrt_lrt_graph.add_edge('MRT Cubao', 'Araneta Center-Cubao')
    mrt_lrt_graph.add_edge('Araneta Center-Cubao', 'MRT Cubao')

    # LRT Line 1
    mrt_lrt_graph.add_edge('Baclaran', 'EDSA')
    mrt_lrt_graph.add_edge('EDSA', 'Libertad')
    mrt_lrt_graph.add_edge('Libertad', 'Gil Puyat')
    mrt_lrt_graph.add_edge('Gil Puyat', 'Vito Cruz')
    mrt_lrt_graph.add_edge('Vito Cruz', 'Quirino')
    mrt_lrt_graph.add_edge('Quirino', 'Pedro Gil')
    mrt_lrt_graph.add_edge('Pedro Gil', 'United Nations')
    mrt_lrt_graph.add_edge('United Nations', 'Central Terminal')
    mrt_lrt_graph.add_edge('Central Terminal', 'Carriedo')
    mrt_lrt_graph.add_edge('Carriedo', 'Doroteo Jose')
    mrt_lrt_graph.add_edge('Doroteo Jose', 'Bambang')
    mrt_lrt_graph.add_edge('Bambang', 'Tayuman')

    # LRT Line 1 to LRT Line 2 (interchange at Doroteo Jose)
    mrt_lrt_graph.add_edge('Doroteo Jose', 'Recto')
    mrt_lrt_graph.add_edge('Recto', 'Doroteo Jose')

    # LRT Line 2
    mrt_lrt_graph.add_edge('Recto', 'Legarda')
    mrt_lrt_graph.add_edge('Legarda', 'Pureza')
    mrt_lrt_graph.add_edge('Pureza', 'V. Mapa')
    mrt_lrt_graph.add_edge('V. Mapa', 'J. Ruiz')
    mrt_lrt_graph.add_edge('J. Ruiz', 'Gilmore')
    mrt_lrt_graph.add_edge('Gilmore', 'Betty Go-Belmonte')
    mrt_lrt_graph.add_edge('Betty Go-Belmonte', 'Araneta Center-Cubao')
    mrt_lrt_graph.add_edge('Araneta Center-Cubao', 'Anonas')
    mrt_lrt_graph.add_edge('Anonas', 'Katipunan')
    mrt_lrt_graph.add_edge('Katipunan', 'LRT Santolan')
    mrt_lrt_graph.add_edge('LRT Santolan', 'Marikina')
    mrt_lrt_graph.add_edge('Marikina', 'Antipolo')
    
    #LRT Line 1 and MRT Line 3
    mrt_lrt_graph.add_edge('Taft Avenue', 'EDSA')
    mrt_lrt_graph.add_edge('EDSA', 'Taft Avenue')
    return mrt_lrt_graph


def find_shortest_path(graph, start, end):
    # Perform a Breadth-First Search (BFS) to find the shortest path
    queue = [(start, [])]
    visited = set()

    while queue:
        current_station, path = queue.pop(0)
        path = path + [current_station]

        print(f"Visiting: {current_station}")

        if current_station == end:
            return path

        visited.add(current_station)

        for neighbor in graph.graph[current_station]:
            if neighbor not in visited:
                queue.append((neighbor, path))

        # Special handling for interchange stations
        if current_station == 'Araneta Center-Cubao':
            for neighbor in graph.graph[current_station]:
                if neighbor not in path and neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
        elif current_station == 'Doroteo Jose':
            for neighbor in graph.graph[current_station]:
                if neighbor not in path and neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

    return None  # If no path is found


# Add methods to the Graph class to get forward and reverse neighbors
def get_forward_neighbor(self, station, path):
    for neighbor in self.graph[station]:
        if neighbor not in path:
            return neighbor
    return None

def get_reverse_neighbor(self, station, path):
    for neighbor in self.graph[station]:
        if neighbor not in path:
            return neighbor
    return None

# Add the new methods to the Graph class
Graph.get_forward_neighbor = get_forward_neighbor
Graph.get_reverse_neighbor = get_reverse_neighbor

# Build the MRT and LRT graph
mrt_lrt_graph = build_mrt_lrt_graph()

