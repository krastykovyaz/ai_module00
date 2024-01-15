import numpy as np
import unittest

def predict_(x, theta):
    """Computes the vector of prediction y_hat from two non-empty numpy.array.
    Args:
    x: has to be an numpy.array, a vector of dimension m * 1.
    theta: has to be an numpy.array, a vector of dimension 2 * 1.
    Returns:
    y_hat as a numpy.array, a vector of dimension m * 1.
    None if x and/or theta are not numpy.array.
    None if x or theta are empty numpy.array.
    None if x or theta dimensions are not appropriate.
    Raises:
    This function should not raise any Exceptions.
    """
    try:
        if not all(isinstance(obj, np.ndarray) for obj in [x, theta]):
            return None
        if any(obj.size == 0 for obj in [x, theta]):
            return None
        if (theta.shape != (2, 1)) or (x.shape[1] != 1):
            return None
        
        return np.dot(np.hstack((np.ones((x.shape[0], 1)), x)), theta)
    except Exception as e:
        print(e)
        return None
    


class TestPredictFunction(unittest.TestCase):
    
    def test_predict_example1(self):
        x = np.arange(1, 6).reshape(-1, 1)
        theta1 = np.array([[5], [0]])
        result = predict_(x, theta1)
        expected_result = np.array([[5], [5], [5], [5], [5]])
        self.assertTrue(np.array_equal(result, expected_result))

    def test_predict_example2(self):
        x = np.arange(1, 6).reshape(-1, 1)
        theta2 = np.array([[0], [1]])
        result = predict_(x, theta2)
        expected_result = np.array([[1], [2], [3], [4], [5]])
        self.assertTrue(np.array_equal(result, expected_result))

    def test_predict_example3(self):
        x = np.arange(1, 6).reshape(-1, 1)
        theta3 = np.array([[5], [3]])
        result = predict_(x, theta3)
        expected_result = np.array([[8], [11], [14], [17], [20]])
        self.assertTrue(np.array_equal(result, expected_result))

    def test_predict_example4(self):
        x = np.arange(1, 6).reshape(-1, 1)
        theta4 = np.array([[-3], [1]])
        result = predict_(x, theta4)
        expected_result = np.array([[-2], [-1], [0], [1], [2]])
        self.assertTrue(np.array_equal(result, expected_result))

if __name__ == '__main__':
    unittest.main()

