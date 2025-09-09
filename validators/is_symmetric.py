Fungsi is_symmetric(matriks):
  // 1. Periksa apakah matriks adalah matriks persegi
  Jika matriks.jumlah_baris TIDAK SAMA DENGAN matriks.jumlah_kolom:
    Kembalikan FALSE

  // 2. Periksa apakah elemen (i, j) sama dengan elemen (j, i)
  Untuk setiap baris i dari 0 sampai jumlah_baris - 1:
    Untuk setiap kolom j dari 0 sampai jumlah_kolom - 1:
      Jika matriks.data[i][j] TIDAK SAMA DENGAN matriks.data[j][i]:
	Kembalikan FALSE

  // 3. Jika semua elemen sesuai, matriks adalah simetris
  Kembalikan TRUE
