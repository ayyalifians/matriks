# operations/transpose.py

def transpose(mat):
    """
    mat: list of lists OR Matrix object with .data
    Returns new list of lists (transposed).
    """
    # support Matrix instance
    try:
        data = mat.data
    except AttributeError:
        data = mat
    if not data:
        return []
    return [list(row) for row in zip(*data)]

