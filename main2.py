from matriks.matrix import Matrix
from matriks.operations.buggy_adder import buggy_add

m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[5, 6, 7], [8, 9, 10]])  # matriks dimensi berbeda

print("Hasil Penjumlahan (BUGGY):")
hasil = buggy_add(m1, m2)
print(hasil.data)
