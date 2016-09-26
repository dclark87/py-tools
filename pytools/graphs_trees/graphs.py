# pytools/graphs_trees/graphs.py
#
# Author: Daniel Clark, 2016

'''
This module contains functions to solve problems related to graphs
data structures
'''

class Vertex(object):
    '''
    Vertex of a graph which uses a key and dictionary to store node
    value and adjacent vertices and weights
    '''

    def __init__(self, key):
        '''
        Init the Vertex object
        '''

        # Import packages
        import sys

        # Init instance attributes
        self.key = key
        self.connected_to = {}
        self.color = 'white'
        self.dist = sys.maxsize
        self.pred = None
        self.disc = 0
        self.fin = 0

    def add_neighbor(self, nbr, weight=0):
        '''
        Method to connect self to neighbor vertex with an optional
        weight
        '''
        self.connected_to[nbr] = weight

    def get_connections(self):
        '''
        Get a list of connections of the vertex
        '''
        return self.connected_to.keys()

    def get_weight(self, nbr):
        '''
        Get the weight of a neighbor vertex of self
        '''
        return self.connected_to[nbr]

    def __str__(self):
        '''
        Print vertex connection information
        '''
        weight_str = ' --%.3f--> %s\n'
        connections_str = '\n' + str(self.key)
        for nbr, wght in self.connected_to.items():
            connections_str = connections_str + weight_str % (wght, nbr.key) + \
                              len(str(self.key))*' '
        return connections_str

class Graph(object):
    '''
    Graph class for storing vertices and edge weights between vertices
    '''

    def __init__(self):
        '''
        Init the graph object with a dict for vertices and size of
        graph; vert_dict = {key : Vertex(key)}
        '''
        self.vert_dict = {}
        self.num_vertices = 0

    def add_vertex(self, key):
        '''
        Method to add a new vertex to the graph by specifying a key
        '''

        # Increase size of graph
        self.num_vertices += 1
        # Create and add in new vertex from key
        new_vertex = Vertex(key)
        self.vert_dict[key] = new_vertex

        # Return the vertex object
        return new_vertex

    def get_vertex(self, key):
        '''
        Get the vertex associated with a given key
        '''

        # Try and get the vertex from dict access
        try:
            vertex = self.vert_dict[key]
            return vertex
        except KeyError:
            err_msg = 'Vertex with key: %s not in graph!' % str(key)
            print err_msg
            return None

    def add_edge(self, from_key, to_key, weight=0):
        '''
        Add an edge from one vertex to another by specifying the
        from_key and to_key; optionally the weight can be specified
        as well
        '''

        # If either key is not in graph, add it
        if from_key not in self.vert_dict.keys():
            from_vert = self.add_vertex(from_key)
        if to_key not in self.vert_dict.keys():
            to_vert = self.add_vertex(to_key)

        # Add neighbor connection
        self.vert_dict[from_key].add_neighbor(self.vert_dict[to_key], weight)

    def get_vertices(self):
        '''
        Return a list of vertices by their key value
        '''
        return self.vert_dict.keys()

    def clear_visited(self):
        '''
        Set all colors to white
        '''
        for vert in self.vert_dict.values():
            vert.color = 'white'

    def find_route_dfs(self, start_data, end_data):
        '''
        Find if there exists a route between two nodes
        '''

        # Ensure both nodes are in graph
        if not (start_data in self.vert_dict.keys() and \
                end_data in self.vert_dict.keys()):
            err_msg = 'start data and end data both need to be in graph!'
            raise ValueError(err_msg)

        # Init variables
        found = False
        start_node = self.vert_dict[start_data]
        children = start_node.get_connections()

        # If there are no children or we visited the node already, return false
        if len(children) == 0 or start_node.color != 'white':
            return False
        # Mark node as visited ('grey')
        start_node.color = 'grey'

        # Iterate through all node children, and search depth recursively
        for child in children:
            # If we found end_data key, return True
            if child.key == end_data:
                return True
            # Otherwise, recursively search downward
            found = self.find_route_dfs(child.key, end_data)
            # If we found it on that downward path, break from loop
            if found:
                break

        # Return result of search
        return found

    def __contains__(self, key):
        '''
        Enable in operator to check graph
        '''
        return key in self.vert_dict.keys()

    def __iter__(self):
        '''
        Enable as iterator to return every vertex in graph
        '''
        return iter(self.vert_dict.values())


def build_wordladder_graph(text_filepath):
    '''
    This function builds a word-ladder graph where each word is a
    vertex in the graph and words that differ by exactly one letter
    are connected by an edge (non directional, no weight)

    Parameters
    ----------
    text_filepath : string
        filepath to a text document with a word on each line

    Returns
    -------
    word_graph : Graph object
        a Graph object containing the vertices and connections for
        the word ladder
    '''

    # Init variables
    word_buckets = {}
    word_graph = Graph()

    # With the file open, create dictionary
    with open(text_filepath, 'r') as wfile:
        # For each word in the text file
        for word in wfile:
            word = word.rstrip('\n')
            for let in range(len(word)):
                bucket = word[:let] + '_' + word[let+1:]
                if word_buckets.has_key(bucket):
                    word_buckets[bucket].append(word)
                else:
                    word_buckets[bucket] = [word]

    # Add vertices and edges for words in the same bucket
    for bucket in word_buckets.keys():
        for word1 in word_buckets[bucket]:
            for word2 in word_buckets[bucket]:
                if word1 != word2:
                    word_graph.add_edge(word1, word2)

    # Return the graph
    return word_graph


def breadth_first_search(graph, start_vert):
    '''
    Function to perform a BFS search on a graph given a starting vertex
    '''

    # Import packages
    from pytools.stacks_queues import queues

    # Init variables
    start_vert.dist = 0
    start_vert.pred = None

    # Add starting vertex to Queue
    vert_queue = queues.ListQueue()
    vert_queue.enqueue(start_vert)

    # While the queue is not empty
    while vert_queue.size() > 0:
        # Pop oldest item off queue
        curr_vert = vert_queue.dequeue()
        # Iterate through each of its neighbors
        for nbr_vert in curr_vert.get_connections():
            # If it hasnt been searced (is white)...search
            if nbr_vert.color == 'white':
                nbr_vert.color = 'gray'
                nbr_vert.dist = curr_vert.dist + 1
                nbr_vert.pred = curr_vert
                vert_queue.enqueue(nbr_vert)
        # Once done searching through neighbors, curr_vert is searched
        curr_vert.color = 'black'


def traverse(start_vert):
    '''
    Traverse through a graph that has been searched through by
    specifying a start vertex
    '''

    # Init variables
    curr_vert = start_vert
    # While predecessor exists, traverse through and print keys
    while curr_vert.pred:
        print curr_vert.key
        curr_vert = curr_vert.pred
    # Print ultimate parent vertex
    print curr_vert.key


class DFSGraph(Graph):
    '''
    A depth-first search (DFS) graph
    '''

    def __init__(self):
        '''
        Init the DFS Graph obj
        '''
        super(DFSGraph, self).__init__()
        self.time = 0

    def _dfs_visit(self, start_vertex):
        '''
        Recursive function for visiting a vertex
        '''

        # Mark vertex as pending, and incr time
        start_vertex.color = 'gray'
        self.time += 1
        start_vertex.disc = self.time
        for other_vertex in start_vertex.get_connections():
            if other_vertex.color == 'white':
                other_vertex.pred = start_vertex
                # Recursively visit first other neighbor
                self._dfs_visit(other_vertex)
        start_vertex.color = 'black'
        self.time += 1
        start_vertex.fin = self.time

    def depth_first_search(self):
        '''
        Perform a depth-first search
        '''

        # Init all to white - unseen
        for each_vertex in self:
            each_vertex.color = 'white'
            each_vertex.pred = None
        for each_vertex in self:
            if each_vertex.color == 'white':
                self._dfs_visit(each_vertex)
