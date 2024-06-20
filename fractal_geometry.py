import numpy as np

def sierpinski_gasket(n):
    """Generate points of the Sierpinski gasket fractal."""
    points = np.array([[0, 0], [1, 0], [0.5, np.sqrt(3)/2]])
    for i in range(n):
        new_points = []
        for p in points:
            for q in points:
                if np.random.random() < 0.5:
                    new_points.append(0.5 * (p + q))
        points = np.array(new_points)
    return points

# Visualize the discontinuous, self-similar structure
import matplotlib.pyplot as plt
points = sierpinski_gasket(10)
plt.scatter(points[:, 0], points[:, 1], s=0.1)
plt.show()
