import numpy as np
import matplotlib.pyplot as plt
plt.ion()   # force interactive plots


class ChaosGame():
    def __init__(self, n, r=0.5):
        if not isinstance(n, int):
            raise ValueError("n must be an integer")
        if not isinstance(r, float):
            raise ValueError("r must be a floating-point number")
        if n < 3:
            raise ValueError("n must be greater than or equal to 3")
        if r <= 0 or r >= 1:
            raise ValueError("r must be in range (0, 1)")

        self.n, self.r = n, r
        self._generate_ngon()

    def _generate_ngon(self):
        """Generate corners of n-gon."""
        theta = np.linspace(0, 2*np.pi, self.n, endpoint=False)
        corners = np.empty(shape=(2, self.n))
        corners[0], corners[1] = np.sin(theta), np.cos(theta)
        self.corners = np.transpose(corners)

    def plot_ngon(self):
        """Plot n-gon corners."""
        plt.figure()
        plt.scatter(*zip(*self.corners))
        plt.axis("equal")


if __name__ == "__main__":
    for n in range(3, 9):
        cg = ChaosGame(n)
        cg.plot_ngon()
    plt.show()
