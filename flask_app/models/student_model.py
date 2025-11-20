# flask_app/models/student_model.py
import csv
import numpy as np
from regression.linear_regression import LinearRegression

class StudentModel:
    """
    Model untuk memuat dataset mahasiswa dan
    melakukan prediksi menggunakan Linear Regression.
    """

    def __init__(self, data_path="flask_app/data/student_scores.csv"):
        self.data_path = data_path
        self.X = []
        self.y = []
        self.model = LinearRegression()

    def load_data(self):
        """Membaca data CSV ke X (lama_belajar) dan y (nilai)"""
        with open(self.data_path, newline='') as f:
            reader = csv.DictReader(f)
            self.X, self.y = [], []
            for row in reader:
                self.X.append([float(row["lama_belajar"])])
                self.y.append(float(row["nilai"]))

    def train_model(self):
        """Melatih model Linear Regression dengan data yang dimuat"""
        if not self.X or not self.y:
            self.load_data()
        self.model.fit(self.X, self.y)

    def get_predictions(self):
        predicted = self.model.predict(self.X)
        X_flat = np.array(self.X).flatten()  # pastikan bentuknya array NumPy
        result = []
        for x, y_true, y_pred in zip(X_flat, self.y, predicted):
            result.append({"x": x, "y_true": y_true, "y_pred": y_pred})
        return result

