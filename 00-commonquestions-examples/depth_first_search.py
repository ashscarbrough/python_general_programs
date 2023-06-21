'''
Python program to print DFS traversal from a given  graph
Time complexity: O(Vertices + Edges) : O(N)
'''

from collections import defaultdict

class Graph:
    '''
    This class creates directed graph using adjacency list representation
    '''

    def __init__(self):
        self.graph = defaultdict(list)  # Default dictionary to store graph

    def add_edge(self, vertex_item, edge):
        '''
        Function to add an edge to graph
        '''
        self.graph[vertex_item].append(edge)


    # A function used by DFS
    def depth_first_search_util(self, vertex, visited):
        '''
        A function used by depth first search to account for visited graph neighbors
        '''

        # Mark the current node as visited and print it
        visited.add(vertex)
        print(vertex, end=' ')

        # Recur for all the vertices adjacent to this vertex
        for neighbour in self.graph[vertex]:
            if neighbour not in visited:
                self.depth_first_search_util(neighbour, visited)


    def depth_first_search(self, vertex):
        '''
        The function to do DFS traversal. It uses recursive depth_first_search_util()
        '''

        # Create a set to store visited vertices
        visited = set()

        # Call the recursive helper function
        # to print DFS traversal
        self.depth_first_search_util(vertex, visited)


# Driver's code
if __name__ == "__main__":
    graph = Graph()
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(2, 3)
    graph.add_edge(3, 3)

    print("Following is Depth First Traversal (starting from vertex 2)")

    # Function call
    graph.depth_first_search(2)
