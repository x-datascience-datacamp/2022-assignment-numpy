"""Assignment - using numpy and making a PR.

The goals of this assignment are:
    * Use numpy in practice with two easy exercises.
    * Use automated tools to validate the code (`pytest` and `flake8`)
    * Submit a Pull-Request on github to practice `git`.

The two functions below are skeleton functions. The docstrings explain what
are the inputs, the outputs and the expected error. Fill the function to
complete the assignment. The code should be able to pass the test that we
wrote. To run the tests, use `pytest test_numpy_question.py` at the root of
the repo. It should say that 2 tests ran with success.

We also ask to respect the pep8 convention: https://pep8.org.
This will be enforced with `flake8`. You can check that there is no flake8
errors by calling `flake8` at the root of the repo.
"""
import numpy as np


def max_index(X):
    """Return the index of the maximum in a numpy array.

    Parameters
    ----------
    X : ndarray of shape (n_samples, n_features)
        The input array.

    Returns
    -------
    (i, j) : tuple(int)
        The row and columnd index of the maximum.

    Raises
    ------
    ValueError
        If the input is not a numpy array or
        if the shape is not 2D.
    """
    if not isinstance(X, np.ndarray):
        raise ValueError("Input must be a numpy array.")
    if X.ndim != 2:
        raise ValueError("Input array must be 2D.")
    
    i = 0
    j = 0

    # TODO
    # Initialize variable for maximum value to the value of the element at the first row and first column
    max_value = X[0, 0]
    # Loop through rows and columns of the array
    for k in range(X.shape[0]):
        for l in range(X.shape[1]):
            # Update row, column, and maximum value if current element is greater than the current maximum value
            if X[k, l] > max_value:
                i = k
                j = l
                max_value = X[k, l]     
    # Return row and column indices of the maximum element in X     
    return i, j


def wallis_product(n_terms):
    """Implement the Wallis product to compute an approximation of pi.

    See:
    https://en.wikipedia.org/wiki/Wallis_product

    Parameters
    ----------
    n_terms : int
        Number of steps in the Wallis product. Note that `n_terms=0` will
        consider the product to be `1`.

    Returns
    -------
    pi : float
        The approximation of order `n_terms` of pi using the Wallis product.
    """
    # XXX : The n_terms is an int that corresponds to the number of
    # terms in the product. For example 10000.
    
    # Initialize the product to 1
    product = 1
    # Loop over the range of n_terms
    for i in range(1, n_terms + 1):
        # Update the product with the next term in the series
        product *= 2 * i / (2 * i - 1) * 2 * i / (2 * i + 1)
    # Return the product multiplied by 2
    return product * 2

# Pi approximation of order 16
print(wallis_product(1000)) 


