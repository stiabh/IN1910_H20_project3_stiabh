import numpy as np
import matplotlib.pyplot as plt


class AffineTransform():
    def __init__(self, a=0, b=0, c=0, d=0, e=0, f=0):
        self.a, self.b, self.c, self.d, self.e, self.f = a, b, c, d, e, f

    def __call__(self, point):
        """Return point resulting from affine transformation."""
        if not isinstance(point, (list, tuple, np.ndarray)):
            raise ValueError("Point must be array-like")

        a, b, c, d, e, f = self.a, self.b, self.c, self.d, self.e, self.f
        return np.dot(np.array([[a, b], [c, d]]), point) + np.array([e, f])


def random_func(functions, p_cumulative):
    """Pick random function based on cumulative probabilities."""
    r = np.random.random()
    for j, p in enumerate(p_cumulative):
        if r < p:
            return functions[j]


if __name__ == "__main__":
    barnsley = [(0, 0, 0, 0.16, 0, 0),
                (0.85, 0.04, -0.04, 0.85, 0, 1.60),
                (0.20, -0.26, 0.23, 0.22, 0, 1.60),
                (-0.15, 0.28, 0.26, 0.24, 0, 0.44)]

    functions = []
    for args in barnsley:
        functions.append(AffineTransform(*args))

    # Barnsley probablities:
    barnsley_prob = (0.01, 0.85, 0.07, 0.07)
    # Verify that probabilities sum to 1:
    assert np.sum(barnsley_prob) == 1

    p_cumulative = np.cumsum(barnsley_prob)

    # Iterating the Fern:
    n = 50000
    X = np.zeros(shape=(n, 2))

    for i in range(n-1):
        f = random_func(functions, p_cumulative)
        X[i+1] = f(X[i])