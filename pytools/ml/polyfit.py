# polyfit.py
#
# Author: Daniel Clark, 2015

'''
This module contains functions to fit a polynomial to input data

Usage: python polyfit.py [-m <order_of_poly>] [-i <path_to_input_npy>]
                         [-t <path_to_target_npy>]
'''

# Polynomial fit function
def calc_coeffs(input_data, target_data, poly_order):
    '''
    Function to calculate the polynomial equation coefficients of the
    best-fit line (using a sum-of-squares error function) from the
    input data and target data using matrix algebra

    Parameters
    ----------
    input_data : numpy.ndarray
        array of input data
    target_data : numpy.ndarray
        array of target data for corresponding input data
    poly_order : integer
        the order of the polynomial equation

    Returns
    -------
    w_star : numpy.ndarray
        the polynomial equation weights of the best-fit line; this is a
        column vector of (poly_order+1 x 1) dimensions
    x_mat : numpy.ndarray
        the tile'd input matrix where the input data is repeated
        poly_order+1 times (columns), where each column is raised to
        the power of its column index
        (e.g. 0th col, x_n^0, ..., Mth col x_n^M)
    '''

    # Import packages
    import numpy as np

    # Init variables
    x_mat = np.tile(input_data.transpose(), (1, poly_order+1))

    # Populate matrix X
    for col in range(poly_order+1):
        x_mat[:, col] = x_mat[:, col]**col

    # Create A = X^T*X
    a_mat = np.dot(x_mat.transpose(), x_mat)

    # Calculate b
    b_vec = np.dot(target_data, x_mat).transpose()

    # w* = A^-1 * b
    amat_inv = np.linalg.inv(a_mat)
    w_star = np.dot(amat_inv, b_vec)

    # Return w* and X
    return w_star, x_mat


# Generate input toy data
def generate_input(num_pts, rnd_seed=0, show_plot=False):
    '''
    Function to generate noisy input data using the function
    f(x) = 7*sin(2*PI*x) + N(0, 1) where N(0,1) is the standard normal
    distribution

    Parameters
    ----------
    num_pts : integer
        the number of time points to sample the data
    rnd_seed : integer (optional); defualt=0
        seed for random number generator; if this is set to any number
        that is non-zero, the noisy data will be from a fixed pdf
    show_plot : boolean (optional); default=False
        flag to indicate whether to display the generated data

    Returns
    -------
    input_data : numpy.ndarray
        real-valued observed input data, x_1...x_n
    target_data : numpy.ndarray
        target values from the using f(x) on the input data, t_1...t_n
    '''

    # Import packages
    import matplotlib.pyplot as plt
    import numpy as np

    # Init variables
    PI = np.pi
    input_data = np.arange(1, step=1.0/num_pts)

    # Seed random number generator
    if rnd_seed != 0:
        np.random.seed(rnd_seed)

    # Ensure row vector
    input_data = np.reshape(input_data, (1, num_pts))

    # Generate noisy data
    target_data = 7*np.sin(2*PI*input_data) + np.random.randn(num_pts)

    # Check whether to plot data
    if show_plot:
        plt.plot(input_data, target_data, 'bo')
        plt.xlabel('time points, t')
        plt.ylabel('f(t)')
        plt.show()

    # Return the input data
    return input_data, target_data


# Plot data
def plot_data(x_mat, target_data, w_star):
    '''
    Function to plot input, target, and best-fit data

    Parameters
    ----------
    x_mat : numpy.ndarray
        a (N x poly_order+1) matrix with the input data tiled along
        the column axis (used in calculating w_star via matrix algebra)
    target_data : numpy.ndarray
        a vector of length N of the target data
    '''

    # Import packages
    import matplotlib.pyplot as plt
    import numpy as np

    # Init variables
    num_pts, poly_order = np.shape(x_mat)
    input_data = x_mat[:, 1]

    # Calculate the best-fit line
    best_fit = np.dot(x_mat, w_star)

    # Plot
    plt.plot(input_data.flatten(), target_data.flatten(), 'bo',
             input_data.flatten(), best_fit.flatten(), 'r')
    plt.xlabel('input data, x')
    plt.ylabel('target data, y')
    plt.title('Polynomial fit, M = %d, N = %d' % (poly_order-1, num_pts))
    plt.show()


# Calculate polynomial weights and plot best fit
def main(poly_order, input_data, target_data):
    '''
    Function to take input and target data, fit a polynomial line to
    the data and plot the result

    Parameters
    ----------
    poly_order : integer
        the order of the polynomial to fit to the data
    input_data : numpy.ndarray
        input data points to use
    target_data : numpy.ndarray
        target data points to use

    Returns
    -------
    None
        this function finds the best-fit and shows a plot
    '''

    # Init variables
    num_pts = 100

    # If input is not specified, generate noisy input
    if not input_data:
        input_data, target_data = generate_input(num_pts, show_plot=False)

    # Calculate w* and X
    w_star, x_mat = calc_coeffs(input_data, target_data, poly_order)

    # Print weight vector
    print 'Weight vector for polynomial:'
    print w_star

    # Plot the data
    plot_data(x_mat, target_data, w_star)

    # Return the weights vector
    return w_star


# Make executable
if __name__ == '__main__':

    # Import packages
    import argparse
    import numpy as np
    import sys

    # Init argparser
    parser = argparse.ArgumentParser(description=__doc__)

    # Init arguments
    parser.add_argument('-m', '--order', nargs=1, required=False,
                        help='Order of polynomial to fit to data')
    parser.add_argument('-i', '--input', nargs=1, required=False,
                        help='Path to .npy file with input data to fit')
    parser.add_argument('-t', '--target', nargs=1, required=False,
                        help='Path to .npy file with target data to fit')

    # Parse arguments
    args = parser.parse_args()

    # Init argument variables
    try:
        poly_order = int(args.order[0])
        if poly_order < 1:
            print 'Polynomial order must be >= 1!\nSpecified: %d' % poly_order
            sys.exit()
    except TypeError as exc:
        poly_order = 5
        print 'No variable specified for polynomial order; default = %d' \
              % poly_order
    try:
        input_data = np.load(args.input[0])
        target_data = np.load(args.target[0])
    except IOError as exc:
        print 'Could not import data.\nError: %s' % exc
    except TypeError as exc:
        input_data = None
        target_data = None
        print 'Data files were not specified; generating default input = '\
              't = 7*sin(2*pi*x) + N(0,1)'

    # Run main routine
    w_star = main(poly_order, input_data, target_data)
