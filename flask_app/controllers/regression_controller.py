# flask_app/controllers/regression_controller.py
from flask import render_template
from flask import Blueprint
from flask import jsonify
from flask import request
from flask import redirect, url_for
from flask import current_app
from models.student_model import StudentModel

# Gunakan Blueprint agar Flask modular
regression_bp = Blueprint("regression", __name__)

class RegressionController:
    """
    Controller untuk menangani request terkait regresi mahasiswa.
    """

    def __init__(self):
        self.model = StudentModel()

    def home(self):
        """Menampilkan halaman utama dengan data regresi"""
        self.model.train_model()
        data = self.model.get_predictions()
        return render_template("index.html", data=data)

# Daftarkan route-nya
controller = RegressionController()

@regression_bp.route("/")
def index():
    return controller.home()
