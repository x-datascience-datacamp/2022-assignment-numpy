
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
    if not isinstance(X, np.ndarray):
        raise ValueError("X must be a numpy array")
    if X.ndim != 2:
        raise ValueError("X must be a 2D array")

    max_val = np.max(X)
    k, h = np.where(X == max_val)
    i, j = k[0], h[0]

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
    pi = 1
    for i in range(1, n_terms+1):
        pi *= (2*i) / (2*i - 1) * (2*i) / (2*i + 1)
    return pi * 2