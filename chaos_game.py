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

    def _starting_point(self):
        """Return random starting point within n-gon."""
        w = np.random.random(self.n)
        w = 1/np.sum(w)*w
        X0 = np.zeros(2)
        for i in range(self.n):
            X0 = np.add(X0, w[i]*self.corners[i])
        return X0

    def iterate(self, steps, discard=5):
        """Generate a number of points using chaos game algorithm."""
        n, r, c = self.n, self.r, self.corners
        x = self._starting_point()

        # Discard points:
        for i in range(discard+1):
            j = np.random.randint(n)
            x = r*x + (1-r)*c[j]

        # Save "steps" next points:
        X = np.empty(shape=(steps, 2))
        J = np.empty(steps)
        X[0], J[0] = x, j

        for i in range(steps-1):
            j = np.random.randint(3)
            X[i+1] = r*X[i] + (1-r)*c[j]
            J[i+1] = j

        self.X, self.J = X, J

    def plot_ngon(self):
        """Plot n-gon corners."""
        plt.figure()
        plt.scatter(*zip(*self.corners))
        plt.axis("equal")


if __name__ == "__main__":
    # for n in range(3, 9):
    # cg = ChaosGame(n)
    # cg.plot_ngon()
    # plt.show()

    cg = ChaosGame(5)
    p = 1000
    X = np.empty(shape=(p, 2))
    for i in range(p):
        X[i] = cg._starting_point()
    cg.plot_ngon()
    plt.scatter(*zip(*X), c="r")
    plt.show()
