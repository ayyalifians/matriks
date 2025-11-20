# flask_app/controllers/regression_controller.py
from flask import render_template, Blueprint, request, jsonify
from flask_app.models.student_model import StudentModel

regression_bp = Blueprint("regression", __name__)

class RegressionController:
    def __init__(self):
        self.model = StudentModel()

    def home(self):
        """
        Menampilkan halaman utama, grafik regresi, dan statistik model.
        Semua variabel yang dibutuhkan template dikirim agar tidak terjadi error Undefined.
        """
        self.model.train_model()

        # Data X dan y
        x_vals = [row[0] for row in self.model.X]     # flatten
        y_true = self.model.y

        # Prediksi menggunakan model
        y_pred = self.model.model.predict([[x] for x in x_vals])

        # Statistik regresi
        intercept = float(self.model.model.coef_[0])
        slope = float(self.model.model.coef_[1])
        r2 = float(self.model.model.score(self.model.X, self.model.y))

        return render_template(
            "index.html",
            x_vals=x_vals,
            y_true=y_true,
            y_pred=y_pred,
            intercept=intercept,
            slope=slope,
            r2_score=round(r2, 4),
            prediction=None   # default halaman awal
        )

    def predict(self):
        """
        API untuk memproses input user (lama belajar) dan mengembalikan prediksi nilai.
        Digunakan oleh AJAX pada index.html.
        """
        try:
            lama_belajar = float(request.form.get("lama_belajar"))
            pred = float(self.model.model.predict([[lama_belajar]])[0])

            return jsonify({
                "lama_belajar": lama_belajar,
                "prediksi": round(pred, 2)
            })

        except Exception as e:
            return jsonify({"error": str(e)}), 400


controller = RegressionController()

@regression_bp.route("/")
def index():
    return controller.home()

@regression_bp.route("/predict", methods=["POST"])
def predict():
    return controller.predict()
