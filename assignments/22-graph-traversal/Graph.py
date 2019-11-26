#  File: Graph.py

#  Description: Assignment 22 | Graph Traversal

#  Student Name: Matthew Maxwell

#  Student UT EID: mrm5632

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 11-25-2019

#  Date Last Modified: 11-25-2019

class Stack (object):
    # stack constructor
    def __init__ (self):
        self.stack = []

    # add an item to the top of the stack
    def push (self, item):
        self.stack.append (item)

    # remove an item from the top of the stack
    def pop (self):
        return self.stack.pop()

    # check the item on the top of the stack
    def peek (self):
        return self.stack[-1]

    # check if the stack if empty
    def is_empty (self):
        return len (self.stack) == 0

    # return the number of elements in the stack
    def size (self):
        return len (self.stack)


class Queue (object):
    # queue constructor
    def __init__ (self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue (self, item):
        self.queue.append (item)

    # remove an item from the beginning of the queue
    def dequeue (self):
        return self.queue.pop(0)

    # only return the item at the end of the queue
    def get_next_item(self):
        if self.size() > 0:
            return self.queue[0]
        return None

    # check if the queue is empty
    def is_empty (self):
        return len (self.queue) == 0

    # return the size of the queue
    def size (self):
        return len (self.queue)

class Vertex(object):
    # vertex constructor
    def __init__(self, label):
        self.label = label
        self.visited = False

    # handle str representation
    def __str__(self):
        return f"{self.label}"

    # determine if a vertex was visited
    def was_visited(self):
        return self.visited

    # determine the label of the vertex
    def get_label(self):
        return self.label

class Graph (object):
    # graph constructor
    def __init__(self):
        self.vertices = []
        self.adj_matrix = []

    # str representation of a graph
    def __str__(self):
        num_vertices = len(self.vertices)
        total_str = ""
        for i in range(num_vertices):
            for j in range(num_vertices):
                total_str += f"{self.adj_matrix[i][j]} "
            total_str += "\n"
        return total_str[:-2]

    # check if a vertex is already in the graph
    def has_vertex (self, label):
        num_vertices = len(self.vertices)
        for i in range(num_vertices):
            if(label == self.vertices[i].get_label()):
                return True
        return False

    # get index from vertex label
    def get_index (self, label):
        num_vertices = len(self.vertices)
        for i in range(num_vertices):
            if(label == self.vertices[i].get_label()):
                return i
        return -1

    # add a Vertex with a given label to the graph
    def add_vertex (self, label):
        # add to self.vertices if not already in it
        if not self.has_vertex(label):
            self.vertices.append(Vertex(label))

        # add a new column to adjacency matrix
        num_vertices = len(self.vertices)
        for i in range(num_vertices - 1):
            self.adj_matrix[i].append(0)

        # add a new row to adjacenct matrix
        self.adj_matrix.append([0 for i in range(num_vertices)])

    # add weighted directed edge to graph
    def add_directed_edge (self, start_vertex, end_vertex, weight=1):
        self.adj_matrix[start_vertex][end_vertex] = weight

    # add weighted undirected edge to graph
    def add_undirected_edge (self, start_vertex, end_vertex, weight=1):
        self.adj_matrix[start_vertex][end_vertex] = self.adj_matrix[end_vertex][start_vertex] = weight

    # get edge weight between two vertices
    # return -1 if edge does not exist
    def get_edge_weight (self, start_vertex_label, end_vertext_label):
        edge_weight = self.adj_matrix[self.get_index(start_vertex_label)][self.get_index(end_vertext_label)]
        if edge_weight != 0:
            return edge_weight
        return -1

    # get a list of immediate neighbors that you can go to from a vertex
    # return empty list if there are none
    def get_neighbors (self, vertex_label):
        neighbors = []
        vertex_index = self.get_index(vertex_label)
        for i in range(len(self.vertices[vertex_index])):
            if self.vertices[vertex_index][i] != 0:
                neighbors.append(self.vertices[vertex_index][i])
        return neighbors

    # return an unvisited vertex adjacent to vertex v (index)
    def get_adj_unvisited_vertex (self, vertex_index):
        for i in range(len(self.adj_matrix[vertex_index])):
            if self.vertices[i].was_visited() == False and self.adj_matrix[vertex_index][i] != 0:
                return i
        return -1

    # get a copy of the list of vertices
    def get_vertices (self):
        return self.vertices

    # do a depth first search in a graph
    def dfs (self, vertex_index):
        stack = Stack()
        self.vertices[vertex_index].visited = True
        print(self.vertices[vertex_index])
        stack.push(vertex_index)
        while(not stack.is_empty()):
            next_vertex = self.get_adj_unvisited_vertex(stack.peek())
            if next_vertex == -1:
                next_vertex = stack.pop()
            else:
                self.vertices[next_vertex].visited = True
                print(self.vertices[next_vertex])
                stack.push(next_vertex)
        self.reset_visits()

    # do a breadth first search in a graph
    def bfs (self, vertex_index):
        queue = Queue()
        self.vertices[vertex_index].visited = True
        print(self.vertices[vertex_index])
        queue.enqueue(vertex_index)
        while(not queue.is_empty()):
            next_vertex = self.get_adj_unvisited_vertex(queue.get_next_item())
            if next_vertex == -1:
                next_vertex = queue.dequeue()
            else:
                self.vertices[next_vertex].visited = True
                print(self.vertices[next_vertex])
                queue.enqueue(next_vertex)
        self.reset_visits()

    def reset_visits(self):
        for i in range(len(self.vertices)):
            self.vertices[i].visited = False

    # delete an edge from the adjacency matrix
    def delete_edge (self, start_vertex_label, end_vertex_label):
        start_index = self.get_index(start_vertex_label)
        end_index = self.get_index(end_vertex_label)
        self.adj_matrix[start_index][end_index] = self.adj_matrix[end_index][start_index] = 0
        
    # delete a vertex from the vertex list and all edges from and
    # to it in the adjacency matrix
    def delete_vertex (self, vertex_label):
        vertex_index = self.get_index(vertex_label)
        del self.vertices[vertex_index]
        del self.adj_matrix[vertex_index]
        for i in range(len(self.vertices)):
            del self.adj_matrix[i][vertex_index]

def main():
    # open input file
    in_file = open("./graph.txt", "r")

    # read number of vertices
    num_vertices = int(in_file.readline().strip())

    # initialize graph object
    graph = Graph()

    # add vertices to graph
    for i in range(num_vertices):
        vertex_label = in_file.readline().strip()
        graph.add_vertex(vertex_label)

    # read number of edges
    num_edges = int(in_file.readline().strip())

    # add edges to adjacency matrix (as undirected edges in this case)
    for i in range(num_edges):
        edge_data = in_file.readline().strip().split(" ")
        edge_start = int(edge_data[0])
        edge_end = int(edge_data[1])
        edge_weight = 1
        if len(edge_data) > 2:
            edge_weight = int(edge_data[2])
        graph.add_undirected_edge(edge_start, edge_end, edge_weight)

    # print vertices and their corresponding indices for clarity
    print(f"Vertex Indices")
    [print(f"{i} : {graph.vertices[i]}") for i in range(len(graph.get_vertices()))]
    print()

    # test depth first search
    start_vertex = in_file.readline().strip()
    print(f"Depth First Search")
    graph.dfs(graph.get_index(start_vertex))

    # test breadth first search
    print(f"\nBreadth First Search")
    graph.bfs(graph.get_index(start_vertex))

    # test deletion of an edge
    edge_cities = in_file.readline().strip().split(" ")
    graph.delete_edge(edge_cities[0], edge_cities[1])
    print(f"\nDeletion of an edge ({edge_cities[0]}, {edge_cities[1]})")
    print(f"\nAdjacency Matrix\n{graph}")

    # test deletion of a vertex
    target_vertex = in_file.readline().strip()
    graph.delete_vertex(target_vertex)
    print(f"\nDeletion of a vertex ({target_vertex})")
    print(f"\nList of Vertices")
    [print(vertex) for vertex in graph.get_vertices()]
    print(f"\nAdjacency Matrix\n{graph}")

if __name__ == "__main__":
    main()