# flask_app/app.py
import os
import sys

# Tambahkan path root project agar modul regression/ bisa dikenali
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask
from controllers.regression_controller import regression_bp

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
        self.app.run(host="0.0.0.0", debug=True, port=5000)

if __name__ == "__main__":
    app_instance = RegressionApp()
    app_instance.run()
