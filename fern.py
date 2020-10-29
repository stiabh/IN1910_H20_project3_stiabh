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