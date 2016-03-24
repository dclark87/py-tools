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


if __name__ == '__main__':
    unittest.main()