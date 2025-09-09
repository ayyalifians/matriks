Fungsi is_identity(matriks):
  // 1. Periksa apakah matriks adalah matriks persegi
  Jika matriks.jumlah_baris TIDAK SAMA DENGAN matriks.jumlah_kolom:
    Kembalikan FALSE

  // 2. Periksa elemen-elemen matriks
  Untuk setiap baris i dari 0 sampai jumlah_baris - 1:
    Untuk setiap kolom j dari 0 sampai jumlah_kolom - 1:
      // Periksa elemen diagonal
      Jika i SAMA DENGAN j:
	Jika matriks.data[i][j] TIDAK SAMA DENGAN 1:
	  Kembalikan FALSE
      // Periksa elemen non-diagonal
      Lainnya:
	Jika matriks.data[i][j] TIDAK SAMA DENGAN 0:
	  Kembalikan FALSE

  // 3. Jika semua elemen sesuai, matriks adalah identitas
  Kembalikan TRUE
