# operations/inverse.py

def inverse(matrix):
    """
    matrix: list of lists (square)
    returns inverse as list of lists.
    Raises ValueError if not square or singular.
    """
    # convert to floats
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("Matrix harus persegi untuk inverse.")

    # create augmented matrix [A | I]
    A = [list(map(float, row)) for row in matrix]
    I = [[float(i == j) for j in range(n)] for i in range(n)]

    # Gauss-Jordan elimination
    for i in range(n):
        # find pivot
        pivot = i
        while pivot < n and abs(A[pivot][i]) < 1e-12:
            pivot += 1
        if pivot == n:
            raise ValueError("Matrix singular; tidak dapat di-inverse.")
        # swap rows i and pivot
        if pivot != i:
            A[i], A[pivot] = A[pivot], A[i]
            I[i], I[pivot] = I[pivot], I[i]

        # normalize row i
        factor = A[i][i]
        A[i] = [x / factor for x in A[i]]
        I[i] = [x / factor for x in I[i]]

        # eliminate other rows
        for r in range(n):
            if r == i:
                continue
            factor = A[r][i]
            A[r] = [a - factor * b for a, b in zip(A[r], A[i])]
            I[r] = [u - factor * v for u, v in zip(I[r], I[i])]

    return I

