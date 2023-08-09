# Graphs:

A graph is a data structure that consists of a set of nodes (vertices) connected by edges. Graphs can represent various relationships between objects and are widely used in various applications like social networks, transportation systems, and more.

## Analogy:

Imagine a social network where people (vertices) are connected by friendships (edges). Each person can have multiple friends, and those friendships can go in both directions.

#### Detail Explanation:

A graph consists of vertices and edges. Each vertex can have zero or more adjacent vertices connected by edges. Edges represent connections between vertices. Neighbors of a vertex are its adjacent vertices, and the degree of a vertex indicates the number of edges connected to it.

### Why Graphs:

Graphs are used in various applications, such as modeling relationships in social networks, representing routes in transportation systems, and much more. They're versatile and powerful for capturing complex connections.

##### Different Types of Graphs:

Undirected Graphs: Here, edges have no direction. Imagine friendships in a social network. Friendships are mutual – if A is friends with B, B is also friends with A.

Directed Graphs (Digraphs): Edges have a direction. Think of Twitter followers – if A follows B, it doesn't necessarily mean B follows A.

#### Visualization:

Think of a city with streets as vertices and intersections as edges. You can go in both directions on a street (undirected). On the other hand, a one-way street allows movement in only one direction (directed).

#### Graph Types Based on Connectivity:

Complete Graphs: Every vertex is connected to every other vertex. It's like a gathering where everyone knows everyone else.

Connected Graphs: All vertices have at least one edge connecting them. It's like a group of friends where everyone knows someone else.

Disconnected Graphs: Some vertices might not have any edges, creating isolated parts. It's like groups of people who don't know each other.

###### Acyclic vs. Cyclic:

Acyclic Graphs: No cycles exist. A cycle is a path that starts and ends at the same vertex. Acyclic graphs are like trees – no repeated paths.

Cyclic Graphs: Cycles are present. Think of a loop that brings you back to your starting point. Cyclic graphs are more like circles than trees.

##### Graph Representation:

Graphs can be represented using two main approaches: adjacency matrix and adjacency list.

Adjacency Matrix: In an adjacency matrix, a 2D array is used where each cell (i, j) represents whether there's an edge from vertex i to vertex j.

Adjacency List: In an adjacency list, each vertex maintains a list of its adjacent vertices. This is a more memory-efficient representation, especially for sparse graphs.

Graph Implementation in Python:

Here's an example of implementing an undirected graph using an adjacency list in Python:

python
Copy code
class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)

    def __str__(self):
        return str(self.graph)

# Create a graph
graph = Graph()

# Add vertices
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")

# Add edges
graph.add_edge("A", "B")
graph.add_edge("B", "C")
graph.add_edge("C", "D")
graph.add_edge("D", "A")

# Print the graph
print(graph)
Traversals:

Traversal means exploring all nodes in a graph. Two common methods are Breadth-First Traversal (like searching one level at a time) and Depth-First Traversal (going deep into one branch before exploring others).

Depth-First Search (DFS) Algorithm:

Depth-First Search (DFS) is a graph traversal algorithm that explores as far as possible along each branch before backtracking. It's commonly used to explore or search through all the vertices and edges in a graph.

DFS Walkthrough:

Starting from vertex A:

Visit A.
Explore unvisited adjacent vertex B.
Visit B.
Explore unvisited adjacent vertex C.
Visit C.
Backtrack to B (no more unvisited neighbors).
Backtrack to A (no more unvisited neighbors).
Explore unvisited adjacent vertex D.
Visit D.
Explore unvisited adjacent vertex E.
Visit E.
Backtrack to D (no more unvisited neighbors).
Backtrack to A (no more unvisited neighbors).
The order of visiting vertices in this example would be: A, B, C, D, E.

## Things I want to learn more about: