import numpy as np


def max_index(X):
    """
    Return the index of the maximum in a numpy array.

    Parameters
    ----------
    X : ndarray of shape (n_samples, n_features)
        The input array.

    Returns
    -------
    (i, j) : tuple(int)
        The row and column index of the maximum.

    Raises
    ------
    ValueError
        If the input is not a numpy array or
        if the shape is not 2D.
    """
    if not isinstance(X, np.ndarray):
        raise ValueError("X must be a numpy array.")
    if len(X.shape) != 2:
        raise ValueError("X must be 2D.")

    max_val = X[0][0]
    max_ind = (0, 0)
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            if X[i][j] > max_val:
                max_val = X[i][j]
                max_ind = (i, j)

    return max_ind


def wallis_product(n_terms):
    """
    Implement the Wallis product to compute an approximation of pi.

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
    if n_terms < 0:
        raise ValueError("n_terms must be a non-negative integer.")
    elif n_terms == 0:
        return 2.

    pi = 1.
    for i in range(1, n_terms+1):
        pi *= ((2*i)**2) / ((2*i-1)*(2*i+1))

    return 2 * pi
