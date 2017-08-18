# tests/unit/polyfit_test.py
#
# Author: Daniel Clark, 2015

'''
This module performs unit testing on the polyfit.py module
'''

# Import packages
import unittest
import mltools.polyfit

# Test case for the polyfit module
class PolyFitTestCase(unittest.TestCase):
    '''
    Test case for the polyfit module
    '''

    # setUp method
    def setUp(self):

        # Init variables
        num_pts = 100
        poly_order = 5

        # Grab inputs x_n and targets t_n
        inputs, targets = mltools.polyfit.generate_input(num_pts, 1, False)

        # Assign to testcase
        self.input_data = inputs
        self.target_data = targets
        self.poly_order = poly_order

    # Test calc_coeffs
    def test_calc_coeffs(self):

        # Import packages
        import datetime
        import numpy as np

        # Init variables
        np_inputs = self.input_data.flatten()
        np_targets = self.target_data.flatten()

        # Get numpy's polyfit
        start = datetime.datetime.now()
        w_star_np = np.polyfit(np_inputs, np_targets, self.poly_order)
        np_time = datetime.datetime.now()-start

        # numpy's coeffs are in high>low order, reverse
        w_star_np = np.flipud(w_star_np)

        # Get mltools' polyfit
        start = datetime.datetime.now()
        w_star_ml, x_mat = mltools.polyfit.calc_coeffs(self.input_data,
                                                       self.target_data,
                                                       self.poly_order)
        ml_time = datetime.datetime.now() - start

        # Assert almost equal for each element
        for idx, w_ml in enumerate(w_star_ml):
            w_np = w_star_np[idx]
            self.assertAlmostEqual(w_ml, w_np, places=5)

        # Print run times
        print '\n'
        print 'numpy\'s polyfit took %.5f seconds' % (np_time.total_seconds())
        print 'mltool\'s polyfit took %.5f seconds' % (ml_time.total_seconds())


# Make executable
if __name__ == '__main__':
    unittest.main()
