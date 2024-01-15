import unittest
import numpy as np
import sys
sys.path.append('..')
from ex04.prediction import predict_

def loss_elem_(y, y_hat):
    """
    Description:
    Calculates all the elements (y_pred - y)^2 of the loss function.
    Args:
    y: has to be an numpy.array, a vector.
    y_hat: has to be an numpy.array, a vector.
    Returns:
    J_elem: numpy.array, a vector of dimension (number of the training examples,1).
    None if there is a dimension matching problem between X, Y or theta.
    None if any argument is not of the expected type.
    Raises:
    This function should not raise any Exception.
    """
    if not isinstance(y, np.ndarray) or not isinstance(y_hat, np.ndarray):
        return None

    if y.shape != y_hat.shape:
        return None
    J_elem = np.array([])
    for i_hat, i in zip(y_hat, y):
        J_elem = np.append(J_elem, (i_hat - i) ** 2)
    J_elem = J_elem.reshape(-1, 1)
    return J_elem
    
    
def loss_(y, y_hat):
    """
    Description:
    Calculates the value of loss function.
    Args:
    y: has to be an numpy.array, a vector.
    y_hat: has to be an numpy.array, a vector.
    Returns:
    J_value : has to be a float.
    None if there is a dimension matching problem between X, Y or theta.
    None if any argument is not of the expected type.
    Raises:
    This function should not raise any Exception.
    """
    try:
        J_elem = loss_elem_(y, y_hat)
        J_value = np.mean(J_elem)
        return J_value
    except Exception as e:
        print(e)
        return None


def loss_elem_(y, y_hat):
    return (y_hat - y) ** 2

def loss_(y, y_hat):
    J_elem = loss_elem_(y, y_hat)
    return np.sum(J_elem) / (2 * y.shape[0])

class TestLinearRegression(unittest.TestCase):

    def test_loss_elem(self):
        # Test Example 1
        x1 = np.array([[0.], [1.], [2.], [3.], [4.]])
        theta1 = np.array([[2.], [4.]])
        y_hat1 = predict_(x1, theta1)
        y1 = np.array([[2.], [7.], [12.], [17.], [22.]])
        output1 = loss_elem_(y1, y_hat1)
        expected_output1 = np.array([[0.], [1], [4], [9], [16]])
        self.assertTrue(np.array_equal(output1, expected_output1), f"Test Example 1 failed: {output1}")


    def test_loss(self):
        # Test Example 2
        x2 = np.array([[0.], [1.], [2.], [3.], [4.]])
        theta2 = np.array([[2.], [4.]])
        y_hat2 = predict_(x2, theta2)
        y2 = np.array([[2.], [7.], [12.], [17.], [22.]])
        output2 = loss_(y2, y_hat2)
        expected_output2 = 3.0
        self.assertAlmostEqual(output2, expected_output2, places=6, msg=f"Test Example 2 failed: {output2}")



if __name__ == '__main__':
    unittest.main()
