import numpy as np
import matplotlib.pyplot as plt

def plot(x, y, theta):
    """Plot the data and prediction line from three non-empty numpy.array.
    Args:
    x: has to be an numpy.array, a vector of dimension m * 1.
    y: has to be an numpy.array, a vector of dimension m * 1.
    theta: has to be an numpy.array, a vector of dimension 2 * 1.
    Returns:
    Nothing.
    Raises:
    This function should not raise any Exceptions.
    """
    # Plotting the data points
    plt.scatter(x, y, label='Data Points')

    # Plotting the prediction line
    x_line = np.linspace(min(x), max(x), 100)
    y_line = theta[0] + theta[1] * x_line
    plt.plot(x_line, y_line, color='red', label='Prediction Line')

    # Adding labels and legend
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()

    # Display the plot
    plt.show()

# Data
x = np.arange(1, 6)
y = np.array([3.74013816, 3.61473236, 4.57655287, 4.66793434, 5.95585554])

# Example 1:
theta1 = np.array([[4.5], [-0.2]])
plot(x, y, theta1)

# Example 2:
theta2 = np.array([[-1.5],[2]])
plot(x, y, theta2)

# Example 3:
theta3 = np.array([[3],[0.3]])
plot(x, y, theta3)