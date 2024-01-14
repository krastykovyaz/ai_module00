import unittest
import numpy as np

def add_intercept(x):
    """Adds a column of 1’s to the non-empty numpy.array x.
    Args:
    x: has to be a numpy.array of dimension m * n.
    Returns:
    X, a numpy.array of dimension m * (n + 1).
    None if x is not a numpy.array.
    None if x is an empty numpy.array.
    Raises:
    This function 
    """
    try:
        if not isinstance(x, np.ndarray) or x.size == 0:
            return None
        if len(x.shape) == 1:
            x = x.reshape(-1, 1)
        ones = np.ones((x.shape[0], 1))
        # print(ones)
        return np.hstack((ones, x))
    except Exception as e:
        print(e)
        return None
    


class TestAddIntercept(unittest.TestCase):

    def test_add_intercept_example1(self):
        x1 = np.arange(1, 6)
        result = add_intercept(x1)
        expected_result = np.array([[1., 1.],
                                    [1., 2.],
                                    [1., 3.],
                                    [1., 4.],
                                    [1., 5.]])
        np.testing.assert_array_equal(result, expected_result)


    def test_add_intercept_example4(self):
        x4 = np.arange(1,10).reshape((3,3))
        result = add_intercept(x4)
        expected_result = np.array([[1., 1., 2., 3.],
                            [1., 4., 5., 6.],
                            [1., 7., 8., 9.]])
        np.testing.assert_array_equal(result, expected_result)

    def test_add_intercept_example2(self):
        y = []
        result = add_intercept(y)
        self.assertIsNone(result)  # Should return None for 2D array

    def test_add_intercept_example3(self):
        x3 = np.array([])
        result = add_intercept(x3)
        self.assertIsNone(result)  # Should return None for empty array


if __name__ == '__main__':
    unittest.main()
