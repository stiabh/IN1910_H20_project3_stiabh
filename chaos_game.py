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
