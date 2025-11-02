def is_identity(matrix):
    """
    Periksa apakah sebuah matriks merupakan matriks identitas.
    Syarat: matriks harus berbentuk persegi (jumlah baris = jumlah kolom).
    """
    rows = len(matrix)
    cols = len(matrix[0])

    # 1. Periksa apakah matriks persegi
    if rows != cols:
        return False

    # 2. Periksa setiap elemen
    for i in range(rows):
        for j in range(cols):
            if i == j:  # Elemen diagonal
                if matrix[i][j] != 1:
                    return False
            else:       # Elemen non-diagonal
                if matrix[i][j] != 0:
                    return False

    # 3. Semua elemen sesuai → matriks identitas
    return True
