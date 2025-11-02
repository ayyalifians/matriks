from operations.transpose import transpose
from operations.inverse import inverse

def test_transpose():
    assert transpose([[1,2],[3,4]]) == [[1,3],[2,4]]

def test_inverse_identity():
    I = [[1,0],[0,1]]
    invI = inverse(I)
    assert all(abs(invI[i][j] - I[i][j]) < 1e-9 for i in range(2) for j in range(2))
