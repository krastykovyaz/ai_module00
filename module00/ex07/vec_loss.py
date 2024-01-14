import unittest
import numpy as np

def loss_(y, y_hat):
    """Computes the half mean squared error of two non-empty numpy.array, without any for loop.
    The two arrays must have the same dimensions.
    Args:
    y: has to be an numpy.array, a vector.
    y_hat: has to be an numpy.array, a vector.
    Returns:
    The half mean squared error of the two vectors as a float.
    None if y or y_hat are empty numpy.array.
    None if y and y_hat does not share the same dimensions.
    Raises:
    This function should not raise any Exceptions.
    """
    if y.size == 0 or y_hat.size == 0 or y.shape != y_hat.shape:
        return None

    squared_error = (y - y_hat) ** 2
    mean_squared_error = np.mean(squared_error)
    half_mean_squared_error = 0.5 * mean_squared_error

    return half_mean_squared_error



class TestLossFunction(unittest.TestCase):

    def test_loss_different_vectors(self):
        X = np.array([[0], [15], [-9], [7], [12], [3], [-21]])
        Y = np.array([[2], [14], [-13], [5], [12], [4], [-19]])
        result = loss_(X, Y)
        self.assertAlmostEqual(result, 2.142857142857143)

    def test_loss_same_vector(self):
        X = np.array([[0], [15], [-9], [7], [12], [3], [-21]])
        result = loss_(X, X)
        self.assertAlmostEqual(result, 0.0)


if __name__ == '__main__':
    unittest.main()
