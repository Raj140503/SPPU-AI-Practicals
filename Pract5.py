def add_edge(graph, edge1, edge2):
    """
    Function to add an edge between two vertices in the graph.
    """
    graph[edge1][edge2] = 1  # Setting edge1 to edge2 as 1
    graph[edge2][edge1] = 1  # Setting edge2 to edge1 as 1

def safe_to_assign(i, j, graph, v, color):
    """
    Function to check if it's safe to assign color 'j' to vertex 'i'.
    """
    for k in range(v):
        if graph[i][k] == 1 and color[k] == j:
            return False  # If there's an adjacent vertex already colored 'j', it's not safe
    return True  # If no adjacent vertex is colored 'j', it's safe

def graph_coloring(graph, m, v, i=0, color=None):
    """
    Function to recursively color the graph vertices.
    """
    if color is None:
        color = [-1] * v  # Initializing color list with -1, indicating no color

    if i == v:
        return True  # All vertices are colored, solution found
    
    for j in range(m):  # Try all colors for vertex i
        if safe_to_assign(i, j, graph, v, color):
            color[i] = j  # Assign color 'j' to vertex 'i'
            if graph_coloring(graph, m, v, i + 1, color):
                return True  # If coloring is successful for remaining vertices, return True
            color[i] = -1  # Backtrack if coloring is not successful

    return False  # If no color is possible for vertex i, return False

def main():
    m = 3  # Number of colors
    v = 6  # Number of vertices
    graph = [[0] * v for _ in range(v)]  # Initialize the graph with all zeros

    # Add edges to the graph
    add_edge(graph, 0, 1)
    add_edge(graph, 0, 2)
    add_edge(graph, 0, 3)
    add_edge(graph, 2, 4)
    add_edge(graph, 2, 5)
    add_edge(graph, 3, 5)

    # Check if graph can be colored using 'm' colors
    if graph_coloring(graph, m, v):
        print("Graph can be colored using", m, "colors.")
    else:
        print("Graph cannot be colored using", m, "colors.")

if __name__ == "__main__":
    main()
