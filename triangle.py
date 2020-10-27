import numpy as np
import matplotlib.pyplot as plt

# First two corners of an equilateral triangle:
c0 = np.array([0, 0])
c1 = np.array([1, 0])

# We can use the fact that every angle in an equilateral triangle
# is 60 degrees, or pi/3 radians, to find the coordinates of the
# third corner. Starting in the origin, we have x = cos(pi/3)
# and y = sin(pi/3), which equals:
c2 = np.array([1/2, np.sqrt(3)/2])
corners = [c0, c1, c2]

# Plot corners to confirm triangle is equilateral:
plt.scatter(*zip(*corners))
plt.show()

w = np.random.random(3)            # random weights
w = 1/sum(w)*w                     # weights sum to 1
X = w[0]*c0 + w[1]*c1 + w[2]*c2    # starting point as a lin.comb. of w

# Plot 1000 random points within triangle:
n = 1000
rand_points = np.empty(shape=(n, 2))

for i in range(len(rand_points)):
    w = np.random.random(3)
    w = 1/sum(w)*w
    rand_points[i] = w[0]*c0 + w[1]*c1 + w[2]*c2
    
plt.scatter(*zip(*rand_points), color="r")