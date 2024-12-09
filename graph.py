class Graph:
    def __init__(self):
        """Initialize an empty adjacency list."""
        self.adj_list = {}

    def add_vertex(self, vertex):
        """Add a vertex to the graph."""
        pass

    def add_edge(self, vertex1, vertex2):
        """Add an edge between two vertices in the graph (undirected)."""
        pass

    def remove_vertex(self, vertex):
        """Remove a vertex and its edges from the graph."""
        pass

    def remove_edge(self, vertex1, vertex2):
        """Remove an edge between two vertices in the graph."""
        pass

    def get_neighbors(self, vertex):
        """Return a list of neighbors for a given vertex."""
        pass
    
    def perform_bfs(self, src, end):
        """Perform BFS and return the path from src to end."""
    
    def perform_dfs(self, src, end):
        """Perform DFS and return the path from src to end."""

    def __str__(self):
        """Return a string representation of the adjacency list."""
        pass

# Example usage:
# graph = Graph()
# graph.add_vertex("A")
# graph.add_vertex("B")
# graph.add_edge("A", "B")
# print(graph)
