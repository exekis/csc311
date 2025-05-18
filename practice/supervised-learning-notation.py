import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Data points (x(i), label)
points = np.array([
    [1, 1, 2],  # x^(1)
    [5, 2, 0],  # x^(2)
    [2, 4, 2],  # x^(3)
    [3, 5, 0],  # x^(4)
    [4, 3, 1]   # x^(5)
])

labels = [1, 1, 1, 0, 0]

# Region R: x1 <= 3
in_region = points[:, 0] <= 3

# 3D Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot points in region R (highlighted)
ax.scatter(points[in_region, 0], points[in_region, 1], points[in_region, 2],
           color='green', label='In Region R (x1 ≤ 3)', s=100)

# Plot points outside region R
ax.scatter(points[~in_region, 0], points[~in_region, 1], points[~in_region, 2],
           color='red', label='Outside Region R', s=100, marker='x')

# Annotate each point with its index
for i, (x, y, z) in enumerate(points):
    ax.text(x, y, z, f'{i+1}', fontsize=10, color='black')

ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')
ax.set_zlabel('$x_3$')
ax.set_title('Training Examples in $\\mathbb{R}^3$')
ax.legend()
plt.show()
