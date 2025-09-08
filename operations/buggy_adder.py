from matriks.operations.matrix import Matrix

def buggy_add(m1, m2):
    """
    Menambahkan dua matriks tanpa validasi dimensi.
    BUG: Jika dimensi tidak sama, fungsi ini akan error (IndexError).
    """
    result_data = []
    for i in range(m1.rows):
        row = []
        for j in range(m1.cols):
            row.append(m1.data[i][j] + m2.data[i][j])
        result_data.append(row)
    return Matrix(result_data)
