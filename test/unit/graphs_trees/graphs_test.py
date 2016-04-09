# test/unit/graph_trees/graphs_test.py
#
# Author: Daniel Clark, 2016

'''
Unit test module to perform testing on the g module
'''

# Import packages
import unittest


class VertexTestCase(unittest.TestCase):
    '''
    TestCase for the Vertex class from the graphs.py module
    '''

    # Set up test case
    def setUp(self):
        '''
        Initialize test case with attributes
        '''

        # Init instance attributes
        pass

    def test_add_neighbor_get_attrs(self):
        '''
        Function to test adding neighboring vertices and getting
        various attributes about the vertex, including a string
        representation of it
        '''

        # Import packages
        from pytools.graphs_trees import graphs

        # Init variables
        vertex = graphs.Vertex(21)
        nbr1 = graphs.Vertex(12)
        nbr2 = graphs.Vertex(24)

        # Add in neighbor vertices
        vertex.add_neighbor(nbr1, weight=.4)
        vertex.add_neighbor(nbr2, weight=.2)
        # Assert they are connections
        conns = vertex.get_connections()
        self.assertIn(nbr1, conns)
        self.assertIn(nbr2, conns)

        # Assert weights are correct
        wght1 = vertex.get_weight(nbr1)
        self.assertEqual(wght1, .4)
        wght2 = vertex.get_weight(nbr2)
        self.assertEqual(wght2, .2)

        # Print the vertex and its connections
        print str(vertex)


class GraphTestCase(unittest.TestCase):
    '''
    TestCase for the Graph class from the graphs.py module
    '''

    # Set up test case
    def setUp(self):
        '''
        Initialize test case with attributes
        '''

        # Import packages
        from pytools.graphs_trees import graphs

        # Init variables
        graph = graphs.Graph()

        # Populate graph
        graph.add_vertex('tree')
        graph.add_vertex('root')
        graph.add_vertex('bark')
        graph.add_vertex('leaf')
        graph.add_edge('tree', 'root', 1)
        graph.add_edge('tree', 'bark', 1)
        graph.add_edge('tree', 'leaf', 1)
        graph.add_vertex('beer')
        graph.add_edge('root', 'beer', 1)
        graph.add_vertex('dogfish')
        graph.add_edge('beer', 'dogfish', 1)
        graph.add_vertex('dog')
        graph.add_edge('bark', 'dog')
        graph.add_edge('dog', 'dogfish', 1)
        graph.add_vertex('bite')
        graph.add_edge('bark', 'bite', 1)
        graph.add_edge('dog', 'bite', 1)
        graph.add_vertex('dogwood')
        graph.add_edge('dog', 'dogwood', 1)
        graph.add_edge('dogwood', 'tree', 1)
        graph.add_vertex('leaves')
        graph.add_edge('leaf', 'leaves', 1)
        graph.add_vertex('leaves of grass')
        graph.add_edge('leaves', 'leaves of grass', 1)

        # Set graph attribute
        self.graph = graph


    def test_find_route_dfs(self):
        '''
        Test the find_route via depth-first searching function
        '''

        # Test tree --> dogwood
        route1 = self.graph.find_route_dfs('tree', 'dogwood')
        self.assertTrue(route1)
        self.graph.clear_visited()
        # Test dog --> leaves
        route2 = self.graph.find_route_dfs('dog', 'leaves')
        self.assertTrue(route2)
        self.graph.clear_visited()
        # Test root --> leaf
        route3 = self.graph.find_route_dfs('root', 'leaf')
        self.assertFalse(route3)
        self.graph.clear_visited()


if __name__ == '__main__':
    unittest.main()