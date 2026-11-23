import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    X=np.array(X,dtype=float)
    y=np.array(y)
    XT=X.T
    coefficient=np.linalg.inv(XT@X)@XT@y
    return np.round(coefficient,4).tolist()