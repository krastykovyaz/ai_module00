import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from math import sqrt
import unittest

def mse_(y, y_hat):
    """
    Description:
    Calculate the MSE between the predicted output and the real output.
    Args:
    y: has to be a numpy.array, a vector of dimension m * 1.
    y_hat: has to be a numpy.array, a vector of dimension m * 1.
    Returns:
    mse: has to be a float.
    None if there is a matching dimension problem.
    Raises:
    This function should not raise any Exceptions.
    """
    try:
        if y.shape != y_hat.shape:
            return None
        return np.mean((y_hat-y)** 2)
    except Exception as e:
        print(e)
        return None
    


def rmse_(y, y_hat):
    """
    Description:
    Calculate the RMSE between the predicted output and the real output.
    Args:
    y: has to be a numpy.array, a vector of dimension m * 1.
    y_hat: has to be a numpy.array, a vector of dimension m * 1.
    Returns:
    rmse: has to be a float.
    None if there is a matching dimension problem.
    Raises:
    This function should not raise any Exceptions.
    """
    
    try:
        if y.shape != y_hat.shape:
            return None
        return np.sqrt(mse_(y_hat, y))
    except Exception as e:
        print(e)
        return None
    


def mae_(y, y_hat):
    """
    Description:
    Calculate the MAE between the predicted output and the real output.
    Args:
    y: has to be a numpy.array, a vector of dimension m * 1.
    y_hat: has to be a numpy.array, a vector of dimension m * 1.
    Returns:
    mae: has to be a float.
    None if there is a matching dimension problem.
    Raises:
    This function should not raise any Exceptions.
    """
    try:
        if y.shape != y_hat.shape:
            return None
        return np.mean(np.abs(y_hat-y))
    except Exception as e:
        print(e)
        return None

def r2score_(y, y_hat):
    """
    Description:
    Calculate the R2score between the predicted output and the output.
    Args:
    y: has to be a numpy.array, a vector of dimension m * 1.
    y_hat: has to be a numpy.array, a vector of dimension m * 1.
    Returns:
    r2score: has to be a float.
    None if there is a matching dimension problem.
    Raises:
    This function should not raise any Exceptions.
    """
    try:
        if y.shape != y_hat.shape:
            return None
        mean_y = np.mean(y)
        r_total = np.sum((y-mean_y)**2)
        r_residual = np.sum((y-y_hat)**2)
        return 1 - (r_residual/r_total)
    except Exception as e:
        print(e)
        return None




class TestMetrics(unittest.TestCase):
    def test_mean_squared_error(self):
        x = np.array([0, 15, -9, 7, 12, 3, -21])
        y = np.array([2, 14, -13, 5, 12, 4, -19])

        # Test custom implementation
        mse_result = mse_(x, y)
        self.assertAlmostEqual(mse_result, 4.285714285714286)

        # Test sklearn implementation
        mse_sklearn_result = mean_squared_error(x, y)
        self.assertAlmostEqual(mse_result, mse_sklearn_result)

    def test_root_mean_squared_error(self):
        x = np.array([0, 15, -9, 7, 12, 3, -21])
        y = np.array([2, 14, -13, 5, 12, 4, -19])

        # Test custom implementation
        rmse_result = rmse_(x, y)
        self.assertAlmostEqual(rmse_result, 2.0701966780270626)

        # Test sklearn implementation
        mse_sklearn_result = mean_squared_error(x, y)
        rmse_sklearn_result = sqrt(mse_sklearn_result)
        self.assertAlmostEqual(rmse_result, rmse_sklearn_result)

    def test_mean_absolute_error(self):
        x = np.array([0, 15, -9, 7, 12, 3, -21])
        y = np.array([2, 14, -13, 5, 12, 4, -19])

        # Test custom implementation
        mae_result = mae_(x, y)
        self.assertAlmostEqual(mae_result, 1.7142857142857142)

        # Test sklearn implementation
        mae_sklearn_result = mean_absolute_error(x, y)
        self.assertAlmostEqual(mae_result, mae_sklearn_result)

    def test_r2score(self):
        x = np.array([0, 15, -9, 7, 12, 3, -21])
        y = np.array([2, 14, -13, 5, 12, 4, -19])

        # Test custom implementation
        r2score_result = r2score_(x, y)
        self.assertAlmostEqual(np.round(r2score_result, 4), np.round(0.9681721733858745, 4))

        # Test sklearn implementation
        r2score_sklearn_result = r2_score(x, y)
        self.assertAlmostEqual(r2score_result, r2score_sklearn_result)

if __name__ == '__main__':
    unittest.main()
