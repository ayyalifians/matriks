# flask_app/app.py
from flask import Flask
from flask_app.controllers.regression_controller import regression_bp
from flask_app.models.student_model import StudentModel

class RegressionApp:
    """
    Kelas utama aplikasi Flask berbasis OOP.
    """

    def __init__(self):
        self.app = Flask(__name__)
        self._register_blueprints()

    def _register_blueprints(self):
        """Mendaftarkan semua route controller"""
        self.app.register_blueprint(regression_bp)

    def run(self):
        """Menjalankan aplikasi Flask"""
        self.app.run(debug=True, port=5000)

if __name__ == "__main__":
    app_instance = RegressionApp().app
    app_instance.run()

app = RegressionApp().app
