import unittest
from matrix import Matrix, Vector

class TestMatrixVectorOperations(unittest.TestCase):
    def test_matrix_transpose(self):
        m1 = Matrix([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0]])
        result = m1.T()
        self.assertEqual(result.data, [[0.0, 2.0, 4.0], [1.0, 3.0, 5.0]])
        self.assertEqual(result.shape, (2, 3))

        m2 = Matrix([[0.0, 2.0, 4.0], [1.0, 3.0, 5.0]])
        result = m2.T()
        self.assertEqual(result.data, [[0.0, 1.0], [2.0, 3.0], [4.0, 5.0]])
        self.assertEqual(result.shape, (3, 2))

    def test_matrix_multiplication(self):
        m1 = Matrix([[0.0, 1.0, 2.0, 3.0], [0.0, 2.0, 4.0, 6.0]])
        m2 = Matrix([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0], [6.0, 7.0]])
        result = m1 * m2
        self.assertEqual(result.data, [[28.0, 34.0], [56.0, 68.0]])
        self.assertEqual(result.shape, (2, 2))

    def test_matrix_vector_multiplication(self):
        m1 = Matrix([[0.0, 1.0, 2.0], [0.0, 2.0, 4.0]])
        v1 = Vector([[1], [2], [3]])
        
        result = m1 * v1
        self.assertEqual(result.data, [[8], [16]])
        self.assertEqual(result.shape, (2, 1))

        v2 = Vector([[2], [4], [8]])
        print(m1.data, v2.data)
        result = m1 * v2
        self.assertEqual(result.data, [[20], [40]])
        self.assertEqual(result.shape, (2, 1))


class TestMatrixVectorOperations(unittest.TestCase):
    def test_matrix_creation(self):
        # Test creating a matrix with a list
        matrix1 = Matrix([[1, 2, 3], [4, 5, 6]])
        self.assertEqual(matrix1.data, [[1, 2, 3], [4, 5, 6]])
        self.assertEqual(matrix1.shape, (2, 3))

        # Test creating a matrix with a tuple
        matrix2 = Matrix((3, 2))
        self.assertEqual(matrix2.data, [[0, 0], [0, 0], [0, 0]])
        self.assertEqual(matrix2.shape, (3, 2))

    def test_matrix_addition(self):
        matrix1 = Matrix([[1, 2], [3, 4]])
        matrix2 = Matrix([[5, 6], [7, 8]])
        result = matrix1 + matrix2
        self.assertEqual(result.data, [[6, 8], [10, 12]])

    def test_matrix_subtraction(self):
        matrix1 = Matrix([[5, 6], [7, 8]])
        matrix2 = Matrix([[1, 2], [3, 4]])
        result = matrix1 - matrix2
        self.assertEqual(result.data, [[4, 4], [4, 4]])

    def test_matrix_multiplication(self):
        matrix1 = Matrix([[1, 2], [3, 4]])
        matrix2 = Matrix([[5, 6], [7, 8]])
        result = matrix1 * matrix2
        self.assertEqual(result.data, [[19, 22], [43, 50]])

    def test_vector_dot_product(self):
        vector1 = Vector([[1], [2], [3]])
        vector2 = Vector([[4], [5], [6]])
        result = vector1.dot(vector2)
        self.assertEqual(result, 32)

    def test_vector_addition(self):
        vector1 = Vector([[1], [2], [3]])
        vector2 = Vector([[4], [5], [6]])
        result = vector1 + vector2
        self.assertEqual(result.data, [[5], [7], [9]])

    def test_vector_subtraction(self):
        vector1 = Vector([[5], [6], [7]])
        vector2 = Vector([[1], [2], [3]])
        result = vector1 - vector2
        self.assertEqual(result.data, [[4], [4], [4]])

    def test_vector_multiplication(self):
        vector = Vector([[1], [2], [3]])
        scalar = 2
        result = vector * scalar
        self.assertEqual(result.data, [[2], [4], [6]])

class AdditionalTests(unittest.TestCase):
    def test_matrix_invalid_creation(self):
        # Test creating a matrix with invalid data types
        with self.assertRaises(TypeError):
            matrix = Matrix(123)

        with self.assertRaises(TypeError):
            matrix = Matrix([[1, 2], [3, 'a']])

    def test_vector_invalid_creation(self):
        # Test creating a vector with invalid data types
        with self.assertRaises(TypeError):
            vector = Vector(123)

        with self.assertRaises(TypeError):
            vector = Vector([[1, 2], [3, 'a']])

    def test_matrix_vector_invalid_operations(self):
        matrix = Matrix([[1, 2, 3], [3, 4, 5]])
        vector = Vector([[1], [2]])

        # Test invalid operations between matrix and vector
        with self.assertRaises(ArithmeticError):
            result = matrix + vector

        with self.assertRaises(ArithmeticError):
            result = matrix - vector

        with self.assertRaises(ArithmeticError):
            result = matrix * vector

        # Test invalid operations between vector and matrix
        with self.assertRaises(ArithmeticError):
            result = vector + matrix

        with self.assertRaises(ArithmeticError):
            result = vector - matrix

        with self.assertRaises(ArithmeticError):
            result = vector * matrix



if __name__ == "__main__":
    unittest.main()
