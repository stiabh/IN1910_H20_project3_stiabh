import numpy as np
from numpy import pi, cos, sin, arctan2, sqrt
import matplotlib.pyplot as plt
from chaos_game import *
from matplotlib.animation import FuncAnimation
import time


class Variations():
    def __init__(self, x, y, name):
        self.x, self.y, self.name = x, y, name
        self._func = getattr(Variations, name)

    def transform(self):
        return np.array(self._func(self.x, self.y))

    @classmethod
    def from_chaos_game(cls, chaos_game, name):
        return cls(*np.transpose(chaos_game.X), name)

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
    def _xy_grid(N=50):
        """Output flattened xy-grid."""
        grid_values = np.linspace(-1, 1, N)
        x, y = np.meshgrid(grid_values, grid_values)
        return x.flatten(), y.flatten()

    def _plot_transformations(variations, color="k"):
        """Plot given variations in chosen colors."""
        fig, axs = plt.subplots(2, 2, figsize=(9, 9))

        for i, (ax, variation) in enumerate(zip(axs.flatten(), variations)):
            u, v = variation.transform()
            ax.scatter(u, -v, s=0.2, marker=".", c=color)
            ax.set_title(variation.name)
            ax.axis("equal")
            ax.axis("off")

    def linear_combination_wrap(V1, V2):
        """Return function """
        def lin_comb(w):
            if w < 0 or w > 1:
                raise ValueError("w must be a value between 0 and 1")
            return w*V1.transform() + (1-w)*V2.transform()
        return lin_comb

    def subplot_variations(transformations):
        """Plot figure with four variations."""
        x_values, y_values = _xy_grid()

        variations = [Variations(x_values, y_values, name)
                      for name in transformations]
        _plot_transformations(variations)

    def subplot_variations_chaos_game(transformations, n=3, r=0.5):
        """Plot chaos game output transformed using 4 variations."""
        x_values, y_values = _xy_grid()

        ngon = ChaosGame(n, r)
        ngon.iterate(10000)
        colors = ngon.gradient_color

        variations = [Variations.from_chaos_game(ngon, name)
                      for name in transformations]
        _plot_transformations(variations, color=colors)

    # transformations = ["linear", "handkerchief", "swirl", "disc"]
    # # transformations = ["horseshoe", "diamond", "ex", "fisheye"]
    # subplot_variations(transformations)
    # # fig.savefig("figures/variations_4b.png", dpi=300)
    # subplot_variations_chaos_game(transformations, 6, 1/3)
    # plt.show()

    coeffs = np.linspace(0, 1, 4)
    ngon = ChaosGame(3, 0.5)   
    ngon.iterate(1000)
    n_color = ngon.gradient_color

    variation1 = Variations.from_chaos_game(ngon, "disc")
    variation2 = Variations.from_chaos_game(ngon, "linear")

    variation12 = linear_combination_wrap(variation1, variation2)    
    
    u, v = variation12(0)
    fps = 60
    trim = 1

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set(xlim=(-1, 1), ylim=(-1, 1))
    ax.axis("off")
    scat = ax.scatter(u[::trim], -v[::trim], s=20 , 
                      marker=".", c=n_color[::trim])
    def animate(i):
        # i: [0, frames)
        if i < fps/2:
            w = 2*(i/fps)
        else:
            w = 2*(1-i/fps)
        u, v = variation12(w)
        scat.set_offsets(np.c_[u[::trim], -v[::trim]])

    anim = FuncAnimation(fig, animate, interval=1/fps*2000,
                         frames=fps, repeat=True)
    plt.show()