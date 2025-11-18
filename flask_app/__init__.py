import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from regression.linear_regression import LinearRegression

class StudentModel:
    """
    Model untuk memuat dataset mahasiswa dan
    melakukan prediksi menggunakan Linear Regression.
    """

    def __init__(self, data_path=None):
        # Tentukan path absolut berdasarkan lokasi file ini
        base_dir = os.path.dirname(os.path.abspath(__file__))
        if data_path is None:
            self.data_path = os.path.join(base_dir, "..", "data", "student_scores.csv")
        else:
            self.data_path = data_path

        self.X = []
        self.y = []
        self.model = LinearRegression()
