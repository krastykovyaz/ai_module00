import numpy as np
import unittest


def simple_predict(x, theta):
    """Computes the vector of prediction y_hat from two non-empty numpy.ndarray.
    Args:
    x: has to be an numpy.ndarray, a vector of dimension m * 1.
    theta: has to be an numpy.ndarray, a vector of dimension 2 * 1.
    Returns:
    y_hat as a numpy.ndarray, a vector of dimension m * 1.
    None if x or theta are empty numpy.ndarray.
    None if x or theta dimensions are not appropriate.
    Raises:
    This function should not raise any Exception.
    """
    try:
        if not all([isinstance(obj, np.ndarray) for obj in [x, theta]]):
            return None
        if (theta.shape not in [(2,), (2, 1)]) \
            or len(x) == 0 or x.shape not in [(x.size,), (x.size, 1)]:
            return None
        y_hat = np.zeros(x.shape)
        for i in range(x.shape[0]):
            y_hat[i] = theta[0] + theta[1] * x[i]
        return y_hat
    except Exception as e:
        print(e)
        return None
    

class TestSimplePredict(unittest.TestCase):

    def test_simple_predict_valid(self):
        x = np.array([[1], [2], [3]])
        theta = np.array([[0.5], [0.8]])
        result = simple_predict(x, theta)
        expected_result = np.array([[1.3], [2.1], [2.9]])
        np.testing.assert_array_almost_equal(result, expected_result)

    def test_simple_predict_empty_input(self):
        x = np.array([])
        theta = np.array([[0.5], [0.8]])
        result = simple_predict(x, theta)
        self.assertIsNone(result)

    def test_simple_predict_invalid_dimensions(self):
        x = np.array([[1, 2], [3, 4]])
        theta = np.array([[0.5], [0.8]])
        result = simple_predict(x, theta)
        self.assertIsNone(result)

    def test_simple_predict_invalid_theta_dimensions(self):
        x = np.array([[1], [2], [3]])
        theta = np.array([[0.5]])
        result = simple_predict(x, theta)
        self.assertIsNone(result)

    def test_simple_predict_empty_theta(self):
        x = np.array([[1], [2], [3]])
        theta = np.array([])
        result = simple_predict(x, theta)
        self.assertIsNone(result)

    def test_example_1(self):
        x = np.arange(1, 6)
        theta = np.array([5, 0])
        result = simple_predict(x, theta)
        expected_result = np.array([5., 5., 5., 5., 5.])
        np.testing.assert_array_almost_equal(result, expected_result)

    def test_example_2(self):
        x = np.arange(1, 6)
        theta = np.array([0, 1])
        result = simple_predict(x, theta)
        expected_result = np.array([1., 2., 3., 4., 5.])
        np.testing.assert_array_almost_equal(result, expected_result)

    def test_example_3(self):
        x = np.arange(1, 6)
        theta = np.array([5, 3])
        result = simple_predict(x, theta)
        expected_result = np.array([8., 11., 14., 17., 20.])
        np.testing.assert_array_almost_equal(result, expected_result)

    def test_example_4(self):
        x = np.arange(1, 6)
        theta = np.array([-3, 1])
        result = simple_predict(x, theta)
        expected_result = np.array([-2., -1., 0., 1., 2.])
        np.testing.assert_array_almost_equal(result, expected_result)


if __name__ == '__main__':
    unittest.main()
