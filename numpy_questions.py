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
    i = 0
    j = 0

    # TODO
    """Check if array is of type numpy"""
    if isinstance(X, np.ndarray):

        """"Check if numpy array is 2D dimension"""
        if X.ndim == 2:

            """Initialize the maximum to the first value"""
            Max = X[i][j]

            """Save the indicies in a 1D array"""
            Indicies=[i, j]

            """"Find the index value of the maximum in each column which means finding the row"""
            Columns = np.argmax(X, axis=0)
            print(Columns)

            """"Find the index value of the maximum in each row which means finding the column"""
            Rows = np.argmax(X, axis=1)
            print(Rows)

            """Ititrate over the columns of each row to change the maximum if we have a new bigger value"""
            if len(Columns) >= len(Rows):
                for v in Rows:
                    for w in Columns:
                        if X[w][v] > Max:
                            Indicies[0] = w
                            Indicies[1] = v
                            Max = X[w][v]
        

            """Ititrate over the rows of each column to change the maximum if we have a new bigger value"""
            if len(Rows) > len(Columns):
                for v in Columns:
                    for w in Rows:
                        if X[v][w] > Max:
                            Indicies[0] = v
                            Indicies[1] = w
                            Max = X[v][w]
            
            i = Indicies[0]
            j = Indicies[1]

        else:
            raise ValueError("Numpy Array is not of dimension 2D")

    else:
        raise ValueError("Array is not of type Numpy")

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

    products = 1

    if n_terms == 0:
        return products*2
    else:
        multiplier = 2
        for n_terms in range (n_terms):
            pterm = multiplier/(multiplier-1)
            nterm = multiplier/(multiplier+1)
            products = products*pterm*nterm 
            multiplier = multiplier + 2 
        return products*2
    return 0.