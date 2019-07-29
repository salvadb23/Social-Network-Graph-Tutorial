#!python

"""
Vertex Class
A helper class for the Graph class that defines vertices and vertex neighbors.
"""

from sys import argv
from collections import deque


class Vertex(object):

    def __init__(self, vertex):
        """initialize a vertex and its neighbors
        neighbors: set of vertices adjacent to self,
        stored in a dictionary with key = vertex,
        value = weight of edge between self and neighbor.
        """
        self.id = vertex
        self.neighbors = {}

    def addNeighbor(self, vertex, weight=0):
        """add a neighbor along a weighted edge"""
        if (vertex not in self.neighbors):
            self.neighbors[vertex] = weight

    def __str__(self):
        """output the list of neighbors of this vertex"""
        return str(self.id) + " adjancent to " + str([x.id for x in self.neighbors])

    def getNeighbors(self):
        """return the neighbors of this vertex"""
        return self.neighbors

    def getId(self):
        """return the id of this vertex"""
        return self.id

    def getEdgeWeight(self, vertex):
        """return the weight of this edge"""
        return self.neighbors[vertex]


class Graph:
    def __init__(self):
        """ initializes a graph object with an empty dictionary.
        """
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        """add a new vertex object to the graph with
        the given key and return the vertex
        """
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex

        return newVertex

    def getVertex(self, vertex):
        """return the vertex if it exists"""
        return self.vertList[vertex] if self.vertList[vertex] is not None else False

    def addEdge(self, vertexOne, vertexTwo, cost=0):
        """add an edge from vertex f to vertex t with a cost
        """
        if self.vertList[vertexOne] is None:
            self.addVertex(vertexOne)
        elif self.vertList[vertexTwo] is None:
            self.addVertex(vertexTwo)
        else:
            self.vertList[vertexOne].addNeighbor(
                self.vertList[vertexTwo], cost)

    def BFS(self, vertex):
        """searches the graph and returns the nodes at n level depth"""
        queue = [(vertex, 0)]
        visited = {}
        while queue:
            vertex, level = queue.pop(0)
            if vertex not in visited:
                visited[vertex] = level
            for neighbor in self.vertList[vertex].neighbors:
                if neighbor not in visited:
                    queue.append((neighbor.getId(), level + 1))
        return visited 
    
    def shortest_path(self, vertex_one, vertex_two):
        """searches the graph and returns the nodes at n level depth"""
        queue = [(vertex_one, 0)]
        visited = {}
        while queue:
            vertex, level = queue.pop(0)
            if vertex not in visited:
                visited[vertex] = level
            for neighbor in self.vertList[vertex].neighbors:
                if neighbor.getId() is vertex_two:
                    visited[vertex_two] = level + 1
                    return visited
                if neighbor not in visited:
                    queue.append((neighbor.getId(), level + 1))
        return visited 

    def getVertices(self):
        """return all the vertices in the graph"""
        return self.vertList.keys()

    def __iter__(self):
        """iterate over the vertex objects in the
        graph, to use sytax: for v in g
        """
        return iter(self.vertList.values())

g = Graph()

# Add your friends
g.addVertex(1)
g.addVertex(2)
g.addVertex(3)
g.addVertex(4)
g.addVertex(5)
g.addVertex(6)
g.addVertex(7)
g.addVertex(8)
g.addVertex(9)
g.addVertex(10)

# Add connections (non weighted edges for now)

g.addEdge(1,2)
g.addEdge(1,3)
g.addEdge(2,4)
g.addEdge(2,6)
g.addEdge(2,5)

print(g.shortest_path(1,6)) 