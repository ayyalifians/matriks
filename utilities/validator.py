def is_square(matrix):
    return len(matrix) == len(matrix[0])

def is_symmetric(matrix):
    if not is_square(matrix):
        return False
    return all(matrix[i][j] == matrix[j][i] for i in range(len(matrix)) for j in range(len(matrix)))
