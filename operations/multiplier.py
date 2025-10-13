#Python
#matriks/operations/multiplier.py
from matrix import Matrix

def multiply(A, B):
    """
    Melakukan operasi perkalian matriks.
    Dapat menerima objek Matrix atau list of lists.
    Mengembalikan hasil sebagai list of lists.
    """
    # Ambil data (dukung Matrix atau list biasa)
    try:
        a = A.data
    except AttributeError:
        a = A

    try:
        b = B.data
    except AttributeError:
        b = B

    # Validasi dimensi
    if not a or not b:
        raise ValueError("Matriks tidak boleh kosong.")
    if len(a[0]) != len(b):
        raise ValueError("Jumlah kolom matriks pertama harus sama dengan jumlah baris matriks kedua.")

    # Perkalian matriks
    result = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            total = 0
            for k in range(len(b)):
                total += a[i][k] * b[k][j]
            result[i][j] = total
    return result


# Opsional: tetap sediakan versi lama agar kompatibel dengan kode lama
def multiply_matrices(matrix1, matrix2):
    result = multiply(matrix1, matrix2)
    # Bungkus hasil ke dalam Matrix object supaya tetap backward compatible
    return Matrix(result)
