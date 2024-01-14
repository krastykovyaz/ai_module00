import numpy as np
from typing import Union, List
import unittest



class TinyStatistician:

    @staticmethod
    def mean(lsts: Union[np.ndarray, list])-> float:
        """
    Calculates the mean of the given array.
    
    Parameters:
        x (Union[np.ndarray, list]): Input array containing numerical values.
    
    Returns:
        float: Mean value of the array.
    """
        try:
            if len(lsts) == 0 or not isinstance(lsts, (list, np.ndarray)):
                return None
            m = 0
            for lst in lsts:
                m += lst
            return m / len(lsts)
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def median(lsts: Union[np.ndarray, list]) -> float:
        """
        Calculates the median of the given array.
        
        Parameters:
            x (Union[np.ndarray, list]): Input array containing numerical values.
        
        Returns:
            float: Median value of the array.
        """
        try:
            if len(lsts) == 0 or not isinstance(lsts, (list, np.ndarray)):
                return None
            lsts_sorted = sorted(lsts)
            if len(lsts) % 2 != 0:
                median = lsts_sorted[int(len(lsts) / 2)]
            else:
                f = lsts_sorted[int(len(lsts) / 2) - 1]
                s = lsts_sorted[int(len(lsts) / 2)]          
                median = 0.5 * (f + s)
            return median
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def quartile(lsts: Union[np.ndarray, list]) -> list:
        """
        Calculates the first and third quartiles of the given array.

        Parameters:
            x (Union[np.ndarray, list]): Input array containing numerical values.

        Returns:
            list: List containing the first and third quartiles.
        """
        try:
            return [TinyStatistician.percentile(lsts, percentile) for percentile in (25, 75)]
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def percentile(lsts: Union[np.ndarray, list], p: int) -> float:
        """
        Calculates the specified percentile of the given array.

        Parameters:
            x (Union[np.ndarray, list]): Input array containing numerical values.
            p (int): Desired percentile (between 0 and 100).

        Returns:
            float: The value at the specified percentile in the array.
        """
        try:
            if len(lsts) == 0 or not isinstance(lsts, (list, np.ndarray)):
                return None
            lsts = sorted(lsts)
            m = len(lsts) - 1
            index = m * p / 100

            if index.is_integer():
                return lsts[int(index)]
            down, up = int(index), int(index) + 1
            return lsts[down] * (up - index) + lsts[up] * (index - down)
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def var(lsts: Union[np.ndarray, list]) -> float:
        """
        Calculates the variance of the given array.

        Parameters:
            x (Union[np.ndarray, list]): Input array containing numerical values.

        Returns:
            float: The variance of the array.
        """
        try:
            if len(lsts) == 0 or not isinstance(lsts, (list, np.ndarray)):
                return None
            var = 0
            for lst in lsts:
                var += (lst - TinyStatistician.mean(lsts)) ** 2
            return var / len(lsts)
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def std(lsts: Union[np.ndarray, list]) -> float:
        """
        Calculates the standard deviation of the given array.

        Parameters:
            x (Union[np.ndarray, list]): Input array containing numerical values.

        Returns:
            float: The standard deviation of the array.
        """
        try:
            if len(lsts) == 0 or not isinstance(lsts, (list, np.ndarray)):
                return None
            return np.sqrt(TinyStatistician.var(lsts))
        except Exception as e:
            print(e)
            return None





class TestTinyStatistician(unittest.TestCase):
    def setUp(self):
        self.s = TinyStatistician()

    def test_mean(self):
        data = np.array([10, 7, 4, 3, 2, 1])
        expected_result = np.mean(data)
        self.assertAlmostEqual(expected_result, self.s.mean(data))

    def test_median(self):
        data = np.array([10, 7, 4, 3, 2, 1])
        expected_result = np.median(data)
        self.assertAlmostEqual(expected_result, self.s.median(data))

    def test_quartile(self):
        data = np.array([10, 7, 4, 3, 2, 1])
        expected_result = [np.ceil(np.quantile(data, 0.25)), np.ceil(np.quantile(data, 0.75))]
        result = self.s.quartile(data)
        self.assertEqual(expected_result, result)


    def test_percentile(self):
        data = np.array([10, 7, 4, 3, 2, 1])
        p = 50
        expected_result = int(np.percentile(data, p))
        self.assertAlmostEqual(expected_result, self.s.percentile(data, p))

    def test_var(self):
        data = np.array([10, 7, 4, 3, 2, 1])
        expected_result = np.var(data)
        self.assertAlmostEqual(expected_result, self.s.var(data))

    def test_std(self):
        data = np.array([10, 7, 4, 3, 2, 1])
        expected_result = np.std(data)
        self.assertAlmostEqual(expected_result, self.s.std(data))

    def test_mean(self):
        a = [1, 42, 300, 10, 59]
        result = self.s.mean(a)
        self.assertEqual(result, 82.4)

    def test_median(self):
        a = [1, 42, 300, 10, 59]
        result = self.s.median(a)
        self.assertEqual(result, 42.0)

    def test_quartile(self):
        a = [1, 42, 300, 10, 59]
        result = self.s.quartile(a)
        self.assertEqual(result, [10.0, 59.0])

    def test_percentile(self):
        a = [1, 42, 300, 10, 59]
        result_10 = self.s.percentile(a, 10)
        result_15 = self.s.percentile(a, 15)
        result_20 = self.s.percentile(a, 20)
        self.assertEqual(result_10, 4.6)
        self.assertEqual(result_15, 6.4)
        self.assertEqual(result_20, 8.2)

    def test_var(self):
        a = [1, 42, 300, 10, 59]
        result = self.s.var(a)
        self.assertEqual(np.round(result,1), 12279.4)

    def test_std(self):
        a = [1, 42, 300, 10, 59]
        result = self.s.std(a)
        self.assertEqual(np.round(result,1), 110.8)

if __name__ == '__main__':
    unittest.main()
    t = TinyStatistician()
    a = [10, 7, 4, 3, 2, 1]
    print(t.quartile(a))


