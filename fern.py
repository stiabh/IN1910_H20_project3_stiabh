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


if __name__ == "__main__":
    barnsley = [(0, 0, 0, 0.16, 0, 0),
                (0.85, 0.04, -0.04, 0.85, 0, 1.60),
                (0.20, -0.26, 0.23, 0.22, 0, 1.60),
                (-0.15, 0.28, 0.26, 0.24, 0, 0.44)]
    f1 = AffineTransform(*barnsley[0])
    f2 = AffineTransform(*barnsley[1])
    f3 = AffineTransform(*barnsley[2])
    f4 = AffineTransform(*barnsley[3])
