from regression.linear_regression import LinearRegression

def test_regression_simple():
    X = [[1],[2],[3],[4]]
    y = [3,5,7,9]  # y = 1 + 2*x  -> intercept 1, slope 2
    model = LinearRegression()
    model.fit(X, y)
    coefs = model.coef_
    # intercept ~1, slope ~2
    assert abs(coefs[0] - 1) < 1e-6
    assert abs(coefs[1] - 2) < 1e-6
