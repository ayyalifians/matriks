def is_symmetric(matrix):
    """
    Periksa apakah sebuah matriks simetris.
    Syarat: matriks harus berbentuk persegi (jumlah baris = jumlah kolom).
    """
    rows = len(matrix)
    cols = len(matrix[0])

    # 1. Periksa apakah matriks persegi
    if rows != cols:
        return False

    # 2. Periksa elemen simetris
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != matrix[j][i]:
                return False

    # 3. Semua elemen sesuai → matriks simetris
    return True
