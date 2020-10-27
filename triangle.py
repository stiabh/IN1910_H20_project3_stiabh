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