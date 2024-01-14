import numpy as np
import  matplotlib.pyplot  as plt
import sys
sys.path.append('..')
from ex06.loss import loss_

def plot_with_loss(x, y, theta):
    """Plot the data and prediction line from three non-empty numpy.ndarray.
    Args:
    x: has to be an numpy.ndarray, a vector of dimension m * 1.
    y: has to be an numpy.ndarray, a vector of dimension m * 1.
    theta: has to be an numpy.ndarray, a vector of dimension 2 * 1.
    Returns:
    Nothing.
    Raises:
    This function should not raise any Exception.
    """
    if len(x.shape) == 1:
        x = x.reshape(-1, 1)
    y_pred = np.dot(np.hstack((np.ones((x.shape[0], 1)), x)), theta)
    
    plt.scatter(x, y, label='Data Points')
    plt.plot(x, y_pred, color='red', label='Linear Regression Line')
    loss_value = loss_(y, y_pred) * 2
    plt.title(f'Linear Regression with Loss: {loss_value:.2f}')
    for i, ax in enumerate(x):
        plt.plot([ax, ax], [y[i], y_pred[i]], "r--")
    plt.legend()
    plt.show()

if __name__=='__main__':
    x = np.arange(1,6)
    y = np.array([11.52434424, 10.62589482, 13.14755699, 18.60682298, 14.14329568])
    # Example 1:
    theta1= np.array([18,-1])
    plot_with_loss(x, y,theta1)
    # Example 2:
    theta2 = np.array([14, 0])
    plot_with_loss(x, y,theta2)
    # Example 3:
    theta3 = np.array([12, 0.8])
    plot_with_loss(x, y, theta3)