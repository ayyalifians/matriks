# regression/linear_regression.py
from operations.transpose import transpose
from operations.multiplier import multiply
from operations.inverse import inverse

class LinearRegression:
    """
    Implementasi sederhana algoritma Regresi Linier berbasis operasi matriks.
    """
    def __init__(self, fit_intercept=True, ridge_lambda=0.0):
        self.fit_intercept = fit_intercept
        self.ridge_lambda = ridge_lambda
        self.coef_ = None  # parameter model (β)

    def _add_intercept(self, X):
        if not self.fit_intercept:
            return X
        return [[1.0] + row for row in X]

    def fit(self, X, y):
        """
        Mencari parameter β = (X^T X)^-1 X^T y
        """
        X = self._add_intercept(X)
        y = [[val] if not isinstance(val, list) else val for val in y]
        X_T = transpose(X)
        XTX = multiply(X_T, X)

        # regularisasi ridge optional
        if self.ridge_lambda:
            for i in range(len(XTX)):
                XTX[i][i] += self.ridge_lambda

        XTX_inv = inverse(XTX)
        XTy = multiply(X_T, y)
        beta = multiply(XTX_inv, XTy)
        self.coef_ = [b[0] for b in beta]
        return self

    def predict(self, X):
        if self.coef_ is None:
            raise ValueError("Model belum di-fit.")
        X = self._add_intercept(X)
        beta = [[b] for b in self.coef_]
        y_pred = multiply(X, beta)
        return [row[0] for row in y_pred]
