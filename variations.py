import numpy as np
from numpy import pi, cos, sin, arctan2, sqrt
import matplotlib.pyplot as plt


class Variations():
    def __init__(self, x, y, name):
        self.x, self.y, self.name = x, y, name
        self._func = getattr(Variations, name)

    def transform(self):
        return self._func(self.x, self.y)

    @staticmethod
    def linear(x, y):
        return x, y

    @staticmethod
    def handkerchief(x, y):
        r = sqrt(x**2 + y**2)
        theta = arctan2(x, y)
        return r*sin(theta + r), r*cos(theta - r)

    @staticmethod
    def swirl(x, y):
        r2 = x**2 + y**2
        return x*sin(r2) - y*cos(r2), x*cos(r2) + y*sin(r2)

    @staticmethod
    def disc(x, y):
        r = sqrt(x**2 + y**2)
        theta = arctan2(x, y)
        return theta/pi*sin(pi*r), theta/pi*cos(pi*r)

    @staticmethod
    def horseshoe(x, y):
        r = sqrt(x**2 + y**2)
        return 1/r*(x - y)*(x + y), 1/r*2*x*y

    @staticmethod
    def diamond(x, y):
        r = sqrt(x**2 + y**2)
        theta = arctan2(x, y)
        return sin(theta)*cos(r), cos(theta)*sin(r)

    @staticmethod
    def ex(x, y):
        r = sqrt(x**2 + y**2)
        theta = arctan2(x, y)
        p0 = sin(theta + r)
        p1 = cos(theta - r)
        return r*(p0**3 + p1**3), r*(p0**3 - p1**3)

    @staticmethod
    def fisheye(x, y):
        r = sqrt(x**2 + y**2)
        return 2/(r + 1)*y, 2/(r + 1)*x

if __name__ == "__main__":
    N = 100
    grid_values = np.linspace(-1, 1, N)
    x, y = np.meshgrid(grid_values, grid_values)
    x_values = x.flatten()
    y_values = y.flatten()

    # transformations = ["linear", "handkerchief", "swirl", "disc"]
    transformations = ["horseshoe", "diamond", "ex", "fisheye"]
    variations = [Variations(x_values, y_values, name) 
                  for name in transformations]

    fig, axs = plt.subplots(2, 2, figsize=(9, 9))
    for i, (ax, variation) in enumerate(zip(axs.flatten(), variations)):
        u, v = variation.transform()
        
        ax.plot(u, -v, markersize=0.5, marker=".", linestyle="", color="k")
        ax.set_title(variation.name)
        ax.axis("equal")
        ax.axis("off")

    fig.savefig("figures/variations_4b.png", dpi=300)
    plt.show()