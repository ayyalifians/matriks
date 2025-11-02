# matrix.py

class Matrix:
    """
    Kelas sederhana merepresentasikan matriks sebagai list of lists.
    Sediakan properti rows, cols, dan data (list of lists).
    """
    def __init__(self, data):
        if not isinstance(data, list) or not all(isinstance(row, list) for row in data):
            raise TypeError("Data harus berupa list of lists.")
        if len(data) == 0:
            self.data = []
            self.rows = 0
            self.cols = 0
            return
        self.rows = len(data)
        self.cols = len(data[0])
        if not all(len(row) == self.cols for row in data):
            raise ValueError("Semua baris harus memiliki jumlah kolom yang sama.")
        self.data = data

    def copy(self):
        return Matrix([row[:] for row in self.data])
