# Let's create a 3D plot of a simple linear transformation.
# We will define a transformation matrix and apply it to a vector.

import numpy as np
import matplotlib.pyplot as plt

# Define the original vector
v = np.array([1, 2, 3])

# Define the transformation matrix
# This matrix will rotate the vector 45 degrees around the z-axis
T = np.array([[0.7071, -0.7071, 0],
              [0.7071, 0.7071, 0],
              [0, 0, 1]])

# Apply the transformation
v_transformed = np.dot(T, v)

# Create the plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.quiver(0, 0, 0, v[0], v[1], v[2], color='b', label='Original Vector')
ax.quiver(0, 0, 0, v_transformed[0], v_transformed[1], v_transformed[2], color='r', label='Transformed Vector')
ax.set_xlim([0, 3])
ax.set_ylim([0, 3])
ax.set_zlim([0, 3])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
plt.show()
