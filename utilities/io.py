# utilities/io.py
import csv

def import_matrix_from_csv(path, delimiter=',', has_header=False):
    """
    Mengimpor matriks dari file CSV menjadi list of lists (numerik).

    Parameter:
    ----------
    path : str
        Path ke file CSV (misal: 'data/matriks.csv')
    delimiter : str, default=','
        Pembatas kolom pada CSV (misalnya ',' atau ';')
    has_header : bool, default=False
        Jika True, baris pertama akan dilewati (biasanya untuk header nama kolom)

    Returns:
    --------
    list[list[float]]
        Matriks berupa list of lists berisi nilai float
    """
    rows = []
    with open(path, newline='') as f:
        reader = csv.reader(f, delimiter=delimiter)
        for r in reader:
            if not r:
                continue
            rows.append(r)

    if has_header:
        rows = rows[1:]  # lewati baris pertama (header)

    # ubah string ke float
    data = []
    for row in rows:
        try:
            data.append([float(x) for x in row])
        except ValueError:
            raise ValueError("CSV harus berisi nilai numerik agar bisa dihitung.")

    return data
