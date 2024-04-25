# Breadth First Search:

# Define the graph as an adjacency list
graph = {
  '1' : ['2','5'],
  '2' : ['3', '4'],
  '5' : ['6'],
  '3' : [],
  '4' : ['6'],
  '6' : []
}

# Initialize an empty list to store visited nodes
visited = []
# Initialize an empty queue for BFS traversal
queue = []

# Define the breadth first search function
def breadthFirstSearch(visited, graph, node):
  # Mark the current node as visited and add it to the queue
  visited.append(node)
  queue.append(node)

  # Iterate through the queue until it's empty
  while queue:
    # Dequeue a node from the queue
    current_node = queue.pop(0)
    # Print the current node
    print(current_node, end=" ")

    # Iterate through the neighbors of the current node
    for neighbour in graph[current_node]:
      # If the neighbour has not been visited, mark it as visited and enqueue it
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Print a message indicating the start of BFS
print("Breadth-First Search: ")
# Call the BFS function with the initial node '1'
breadthFirstSearch(visited, graph, '1')

# Depth first search

# Reinitialize the graph for DFS traversal
graph = {
  '1' : ['2','5'],
  '2' : ['3', '4'],
  '5' : ['6'],
  '3' : [],
  '4' : ['6'],
  '6' : []
}

# Initialize an empty set to store visited nodes for DFS
visited = set()

# Define the depth first search function
def depthFirstSearch(visited, graph, node):
    # If the node has not been visited yet
    if node not in visited:
        # Print the current node
        print(node)
        # Mark the node as visited
        visited.add(node)
        # Recursively call DFS for each unvisited neighbor of the current node
        for neighbour in graph[node]:
            depthFirstSearch(visited, graph, neighbour)

# Print a message indicating the start of DFS
print("Depth-First Search")
# Call the DFS function with the initial node '1'
depthFirstSearch(visited, graph, '1')
