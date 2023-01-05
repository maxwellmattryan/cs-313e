class Stack (object):
    # stack constructor
    def __init__ (self):
        self.stack = []

    # return a new copy of the stack
    def copy(self):
        new_stack = Stack()
        new_stack.stack = self.stack[:]
        return new_stack

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

    # handle str representation
    def __str__(self):
        return self.queue

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
        self.in_degree = 0

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
        self.vertices[end_vertex].in_degree += 1
        self.adj_matrix[start_vertex][end_vertex] = weight

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

    # delete a vertex from the vertex list and all edges from and
    # to it in the adjacency matrix
    def delete_vertex (self, vertex_label):
        vertex_index = self.get_index(vertex_label)
        # check and reset in_degrees for all vertices connected to deleted one
        for i in range(len(self.adj_matrix[vertex_index])):
            if(self.adj_matrix[vertex_index][i] != 0):
                self.vertices[i].in_degree -= 1
        del self.vertices[vertex_index]
        del self.adj_matrix[vertex_index]
        for i in range(len(self.vertices)):
            del self.adj_matrix[i][vertex_index]

    # delete an edge from start index to end index
    def delete_directed_edge(self, start_index, end_index):
        self.adj_matrix[start_index][end_index] = 0

    # determine if a directed graph has a cycle
    # this function should return a boolean and not print the result
    def has_cycle (self): # implement via dfs
        if(len(self.vertices) > 0):
            stack = Stack()
            vertex_index = 0
            self.vertices[vertex_index].visited = True
            stack.push(vertex_index)
            while(not stack.is_empty()):
                next_vertex = self.get_adj_unvisited_vertex(stack.peek())
                if next_vertex == -1:
                    next_vertex = stack.pop()
                else:
                    self.vertices[next_vertex].visited = True
                    stack.push(next_vertex)
                    # iterate through stack to see if next_vertex has path to any vertex in stack
                    for i in range(len(self.vertices)):
                        if(self.adj_matrix[next_vertex][i] != 0):
                            if i in stack.stack:
                                return True
            return False
        return False

    # return a list of vertices after a topological sort
    # this function should not print the list
    def toposort (self):
        if(len(self.vertices) > 0):
            vertex_queue = Queue()
            vertex_index = 0 
            # loop and collect all vertices with zero in_degree
            while(True):
                vertex = self.vertices[vertex_index]
                if vertex.in_degree == 0:
                    vertex_queue.enqueue(vertex)
                    self.delete_vertex(vertex.label)
                    if len(self.vertices) == 0:
                        break
                else:
                    vertex_index += 1
                if(vertex_index == len(self.vertices)):
                    vertex_index = 0
            return [vertex.label for vertex in vertex_queue.queue]

    # gets in_degree of a given vertex (requires vertex label)
    def get_in_degree(self, vertex_label):
        vertex_index = self.get_index(vertex_label)
        in_degree = sum([self.adj_matrix[i][vertex_index] for i in range(len(self.vertices))])
        return in_degree

def main():
    # read the file and get num vertices
    in_file = open("./topo.txt", "r")
    num_vertices = int(in_file.readline().strip())

    # initialize the graph object
    graph = Graph()

    # insert vertices from file into graph object
    [graph.add_vertex(in_file.readline().strip()) for i in range(num_vertices)]
        
    # get num edges and read into the graph
    num_edges = int(in_file.readline().strip())
    for i in range(num_edges):
        start_label, end_label = in_file.readline().strip().split(" ")
        start_index = graph.get_index(start_label)
        end_index = graph.get_index(end_label)
        graph.add_directed_edge(start_index, end_index)

    # test if a directed graph has a cycle
    graph = Graph()
    print(f"has_cycle():\n{graph.has_cycle()}\n")

    # test topological sort
    print(f"toposort():\n{graph.toposort()}")

main()