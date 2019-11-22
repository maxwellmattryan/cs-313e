class Graph (object):
    # graph constructor
    def __init__(self):
        ...

    # check if a vertex is already in the graph
    def has_vertex (self, label):
        ...

    # get index from vertex label
    def get_index (self, label):
        ...

    # add a Vertex with a given label to the graph
    def add_vertex (self, label):
        ...

    # add weighted directed edge to graph
    def add_directed_edge (self, start, finish, weight = 1):
        ...

    # add weighted undirected edge to graph
    def add_undirected_edge (self, start, finish, weight = 1):
        ...

    # get edge weight between two vertices
    # return -1 if edge does not exist
    def get_edge_weight (self, fromVertexLabel, toVertexLabel):
        ...

    # get a list of immediate neighbors that you can go to from a vertex
    # return empty list if there are none
    def get_neighbors (self, vertexLabel):
        ...

    # return an unvisited vertex adjacent to vertex v (index)
    def get_adj_unvisited_vertex (self, v):
        ...

    # get a copy of the list of vertices
    def get_vertices (self):
        ...

    # do a depth first search in a graph
    def dfs (self, v):
        ...

    # do a breadth first search in a graph
    def bfs (self, v):
        ...

    # delete an edge from the adjacency matrix
    def delete_edge (self, fromVertexLabel, toVertexLabel):
        ...
    # delete a vertex from the vertex list and all edges from and
    # to it in the adjacency matrix
    def delete_vertex (self, vertexLabel):
        ...

def main():
    print(f"FIXME: Start A22")
    # test depth first search

    # test breadth first search

    # test deletion of an edge

    # test deletion of a vertex

if __name__ == "__main__":
    main()