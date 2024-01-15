class Matrix:
    def __init__(self, *args) -> None:
        self.is_valid(*args)
        self.data = self.get_data(*args)
        self.shape = self.get_shape(*args)

    @staticmethod
    def is_valid(args):
        len_args = len(args)
        if isinstance(args, tuple):
            if len_args != 2:
                raise ValueError("Shape argument has an unexpected size.")
        if not isinstance(args, (tuple, list)):
            raise TypeError("The data type provided is not as expected; it should be a list or a tuple.")
        if isinstance(args, list):
            if any([l for l in args if not isinstance(l, list)]):
                raise TypeError("The data argument contains an unexpected type. There is not just a list")
            if len_args == 0:
                raise ValueError("The length provided for the data argument is not as expected.")
            for arg in args:
                if any([a for a in arg if not isinstance(a, (int, float))]):
                    raise TypeError("The data argument contains an unexpected element type.")
            arg0 = len(args[0])
            if any([len(arg) != arg0 for arg in args]):
                raise ValueError("The data argument has columns of varying lengths.")
        
    def get_data(self, args):
        if isinstance(args, list):
            return args.copy()
        else:
            out = []
            for _ in range(args[0]):
                out.append([0] * args[1])
            return out
        
    def get_shape(self, args):
        if isinstance(args, tuple):
            return args
        else:
            return (len(args), len(args[0]))

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise ArithmeticError("The operand on the right side of the addition operator is not an instance of a matrix.")
        if self.shape != other.shape:
            raise ArithmeticError("Shape needs to be the same.")
        try:
            out = Matrix(self.shape)
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    out.data[i][j] = self.data[i][j] + other.data[i][j]
            return out
        except:
            raise  AttributeError("An issue occurred, and it's possible that the Matrix instance was corrupted before the operation.")
      
    def __sub__(self, other):
        if not isinstance(other, Matrix):
            raise ArithmeticError("The operand on the right side of the addition operator is not an instance of a matrix.")
        if self.shape != other.shape:
            raise ArithmeticError("Shape needs to be the same.")
        try:
            out = Matrix(self.shape)
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    out.data[i][j] = self.data[i][j] - other.data[i][j]
            return out
        except:
            raise  AttributeError("An issue occurred, and it's possible that the Matrix instance was corrupted before the operation.")
    
    def __rsub__(self, other):
        if not isinstance(other, Matrix):
            raise ArithmeticError("The operand on the right side of the addition operator is not an instance of a matrix.")
        if self.shape != other.shape:
            raise ArithmeticError("Shape needs to be the same.")
        try:
            out = Matrix(self.shape)
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    out.data[i][j] = other.data[i][j] - self.data[i][j]
            return out
        except:
            raise  AttributeError("An issue occurred, and it's possible that the Matrix instance was corrupted before the operation.")
    
    def __truediv__(self, other):
        if isinstance(other, Matrix):
            try:
                if other.shape == (1,1):
                    out = Matrix(self.shape)
                    for i in range(self.shape[0]):
                        for j in range(self.shape[1]):
                            out.data[i][j] = self.data[i][j] / other.data[0][0]
                    return out
            except:
                raise ArithmeticError("There seems to be a problem with the divisor. \
                                      It could be due to the Matrix not being of dimension (1x1), \
                                      potential corruption of the Matrix object beforehand, \
                                      or an attempt to divide by zero (Matrix([[0]])).")  
        if not isinstance(other, (int, float)):
            raise ArithmeticError("The issue lies with the right member of the division operator, which should be a scalar.")    
        if isinstance(other, (int, float)) and other == 0:
            raise ZeroDivisionError("Dividing by zero is not a valid or advisable operation.")
        try:
            out = Matrix(self.shape)
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    out.data[i][j] = self.data[i][j] / other.data[i][j]
            return out
        except:
            raise  AttributeError("An issue occurred, and it's possible that the Matrix instance was corrupted before the operation.")
    
    def __rtruediv__(self, other):
        try:
            if self.shape != (1,1):
                raise ArithmeticError("There seems to be a problem with the divisor. \
                                        It could be due to the Matrix not being of dimension (1x1)")
            if isinstance(other, Matrix):
                if self.shape == (1,1):
                    out = Matrix(other.shape)
                    if other.shape == (1,1):
                        out = Matrix(self.shape)
                        for i in range(self.shape[0]):
                            for j in range(self.shape[1]):
                                out.data[i][j] = self.other[i][j] / self.data[0][0]
                        return out
            elif isinstance(other, (int, float)):
                return Matrix([[other / self.data[0][0]]])
            else:
                raise ArithmeticError("The issue lies with the right member of the division operator, which should be a scalar.")    

        except:
            raise  AttributeError("An issue occurred, potential corruption of the Matrix object beforehand, \
                                      or an attempt to divide by zero (Matrix([[0]])).")
        
    def __mul__(self, other):
        if not isinstance(other, (Matrix, int, float, Vector)):
            raise ArithmeticError("The operand on the right side of the multiplication operator should be a Matrix, \
                                  integer, float, or Vector instance.")
        try:
            if isinstance(other, (int, float)):
                out = Matrix(self.shape)
                for i in range(self.shape[0]):
                    for j in range(self.shape[1]):
                        out.data[i][j] = self.data[i][j] * other.data[0][0]
                return out
            elif isinstance(other, Matrix):
                if self.shape[1] == other.shape[0]:
                    out = Matrix((self.shape[0], other.shape[1]))
                    for i in range(self.shape[0]):
                        for k in range(other.shape[1]):
                            for j in range(self.shape[1]):
                                out.data[i][k] += self.data[i][j] * other.data[j][k]
                    return out
                else:
                    raise ArithmeticError("Matrix instances should have matching dimensions for this operation.")
            elif isinstance(other, Vector):
                if self.shape[1] == other.shape[0]:
                    out = Vector(other.shape)
                    for i in range(self.shape[0]):
                        for j in range(self.shape[1]):
                            out.data[i][0] = self.data[i][j] * other[j][0]
                    return out
                else:
                    raise ArithmeticError("Matrix instances should have matching dimensions for this operation.")
        except:
            raise  AttributeError("An issue occurred, potential corruption of the Matrix object beforehand")

    def __rmul__(self, other):
        print('__rmul__M')
        if not isinstance(other, (Matrix, int, float, Vector)):
            raise ArithmeticError("Right operand of the multiplication operator should be a Matrix, \
                                  integer, float, or Vector instance.")
        try:
            if isinstance(other, (int, float)):
                out = Matrix(self.shape)
                for i in range(self.shape[0]):
                    for j in range(self.shape[1]):
                        out.data[i][j] = self.data[i][j] * other
                return out
            elif isinstance(other, Matrix):
                if self.shape[1] == other.shape[0]:
                    out = Matrix((self.shape[0], other.shape[1]))
                    for i in range(self.shape[0]):
                        for k in range(other.shape[1]):
                            for j in range(self.shape[1]):
                                out.data[i][k] += other.data[i][j] * self.data[j][k]
                    return out
                else:
                    raise ArithmeticError("Matrix instances should have matching dimensions for this operation.")
            elif isinstance(other, Vector):
                if self.shape[1] == other.shape[0]:
                    out = Vector(other.shape)
                    for i in range(self.shape[0]):
                        for j in range(self.shape[1]):
                            out.data[i][0] += other.data[i][j] * self.data[j][0]
                    return out
                else:
                    raise ArithmeticError("Matrix instances should have matching dimensions for this operation.")
        except:
            raise  AttributeError("An issue occurred, potential corruption of the Matrix object beforehand")
        
    
    def __str__(self):
        return self.__repr__()


    def __repr__(self):
        try:
            return f"""Matrix([
{'%s'.join([str(line) 
           for line in self.data])}
])""" % '\n'
        except:
            raise AttributeError("An issue occurred, potential corruption.")
    
    def T(self):
        out = Matrix(self.shape[::-1])
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                out.data[j][i] = self.data[i][j]
        return out
        

class Vector(Matrix):
    def __init__(self, *args):
        super().__init__(*args)
        if self.shape[0]==1:
            raise ValueError("The data should be in a format with a dimension size of 1, \
                             either with shape (n, 1) or (1, m).")
    
    def dot(self, v):
        if not isinstance(v, Vector):
            raise TypeError("The dot product can only be applied between Vector objects.")
        if (self.shape != v.shape) or (self.shape[1] != 1):
            raise TypeError("Vectors should have the same dimension \
                            and be represented as 2-column vectors.")
        try:
            out = 0
            for i in range(self.shape[0]):
                out += self.data[i][0] * v.data[i][0]
            return out
        except:
            raise AttributeError("An issue occurred; there might be a prior corruption of the Vector instance before the operation.")
        
    def __add__(self, other):
        if not isinstance(other, Vector):
            raise ArithmeticError("Can only be applied between Vector objects.")
        if self.shape != other.shape:
            raise ArithmeticError("Shapes are not compatible for the specified operation.")
        try:
            out = Vector(self.shape)
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    out.data[i][j] = self.data[i][j] + other.data[i][j]
            return out
        except:
            raise  AttributeError("An issue occurred, potential corruption of the Vector object beforehand")
        
    def __radd__(self, other):
        if not isinstance(other, Vector):
            raise ArithmeticError("Left object should be Vector.")
        if self.shape != other.shape:
            raise ArithmeticError("Shapes are not compatible for the specified operation.")
        try:
            out = Vector(self.shape)
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    out.data[i][j] = other.data[i][j] + self.data[i][j]
            return out
        except:
            raise  AttributeError("An issue occurred, potential corruption of the Vector object beforehand")
        
    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise ArithmeticError("Right object should be Vector.")
        if self.shape != other.shape:
            raise ArithmeticError("Shapes are not compatible for the specified operation.")
        try:
            out = Vector(self.shape)
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    out.data[i][j] = self.data[i][j] - other.data[i][j]
            return out
        except:
            raise  AttributeError("An issue occurred, potential corruption of the Vector object beforehand")
        
    def __rsub__(self, other):
        if not isinstance(other, Vector):
            raise ArithmeticError("Left object should be Vector.")
        if self.shape != other.shape:
            raise ArithmeticError("Shapes are not compatible for the specified operation.")
        try:
            out = Vector(self.shape)
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    out.data[i][j] = other.data[i][j] - self.data[i][j]
            return out
        except:
            raise  AttributeError("An issue occurred, potential corruption of the Vector object beforehand")
        
    def __truediv__(self, other):
        if isinstance(other, Vector):
            try:
                if other.shape == (1,1):
                    out = Vector(self.shape)
                    for i in range(self.shape[0]):
                        for j in range(self.shape[1]):
                            out.data[i][j] = self.data[i][j] / other.data[0][0]
                    return out
            except:
                raise ArithmeticError("There seems to be a problem with the divisor. \
                                      It could be due to the Vector is being not of dimension (1x1), \
                                      potential corruption of the Vector object beforehand, \
                                      or an attempt to divide by zero (Vector([[0]])).")  
        if not isinstance(other, (int, float)):
            raise TypeError("The issue lies with the right member of the division operator, which should be a scalar.")    
        if isinstance(other, (int, float)) and other == 0:
            raise ZeroDivisionError("Dividing by zero is not a valid or advisable operation.")
        try:
            out = Vector(self.shape)
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    out.data[i][j] = self.data[i][j] / other.data[i][j]
            return out
        except:
            raise  AttributeError("An issue occurred, and it's possible that the Vector instance was corrupted before the operation.")
        
    def __rtruediv__(self, other):
        try:
            if self.shape != (1,1):
                raise ArithmeticError("There seems to be a problem with the divisor. \
                                        It could be due to the Vector not being of dimension (1x1)")
            if isinstance(other, Vector):
                if self.shape == (1,1):
                    out = Vector(other.shape)
                    if other.shape == (1,1):
                        out = Vector(self.shape)
                        for i in range(self.shape[0]):
                            for j in range(self.shape[1]):
                                out.data[i][j] = self.other[i][j] / self.data[0][0]
                        return out
            elif isinstance(other, (int, float)):
                return Vector([[other / self.data[0][0]]])
            else:
                raise TypeError("The issue lies with the right member of the division operator, which should be a scalar.")    

        except:
            raise  AttributeError("An issue occurred, potential corruption of the Vector object beforehand, \
                                      or an attempt to divide by zero Vector([[0]])).")
        
    def __mul__(self, other):
        if not isinstance(other, (Matrix, int, float, Vector)):
            raise TypeError("The operand on the right side of the multiplication operator should be a Matrix, \
                                  integer, float, or Vector instance.")
        if ((type(self) != int and type(other) != int) or (type(self) != int and type(other) != int)) \
            and self.shape[1] != other.shape[0]:
            raise ArithmeticError("Dimension mismatch.")
        try:
            if isinstance(other, (int, float)):
                out = Vector(self.shape)
                for i in range(self.shape[0]):
                    for j in range(self.shape[1]):
                        out.data[i][j] = self.data[i][j] * other
                return out
            elif isinstance(other, Matrix):
                if self.shape[1] == other.shape[0]:
                    out = Vector((self.shape[0], other.shape[1]))
                    for i in range(self.shape[0]):
                        for k in range(other.shape[1]):
                            for j in range(self.shape[1]):
                                out.data[i][k] += self.data[i][j] * other.data[j][k]
                    return out
                else:
                    raise ArithmeticError("Matrix instances should have matching dimensions for this operation.")
            elif isinstance(other, Vector):
                if self.shape[1] == other.shape[0]:
                    out = Vector(other.shape)
                    for i in range(self.shape[0]):
                        for j in range(self.shape[1]):
                            out.data[i][0] = self.data[i][j] * other[j][0]
                    return out
                else:
                    raise ArithmeticError("Vector instances should have matching dimensions for this operation.")
        except:
            raise  AttributeError("An issue occurred, potential corruption of the Matrix object beforehand")

    def __rmul__(self, other):
        print('__rmul__V')
        if not isinstance(other, (Matrix, int, float, Vector)):
            raise TypeError("Right operand of the multiplication operator should be a Matrix, \
                                  integer, float, or Vector instance.")
        if ((type(self) != int and type(other) != int) or (type(self) != int and type(other) != int)) \
            and other.shape[1] != self.shape[0]:
            raise ArithmeticError("Dimension mismatch.")
        try:
            if isinstance(other, (int, float)):
                out = Vector(self.shape)
                for i in range(self.shape[0]):
                    for j in range(self.shape[1]):
                        out.data[i][j] = self.data[i][j] * other
                return out
            elif isinstance(other, Vector):
                if other.shape[1] == self.shape[0]:
                    out = Vector((other.shape[0], self.shape[1]))
                    for i in range(other.shape[0]):
                        for k in range(self.shape[1]):
                            for j in range(other.shape[1]):
                                out.data[i][k] += other.data[i][j] * self.data[j][k]
                    return out
                else:
                    raise ArithmeticError("Vector instances should have matching dimensions for this operation.")
            elif isinstance(other, Matrix):
                if other.shape[1] == self.shape[0]:
                    out = Vector((other.shape[0], self.shape[1]))
                    for i in range(other.shape[0]):
                        for j in range(other.shape[1]):
                            out.data[i][0] += (other.data[i][j] * self.data[j][0])
                    return out
                else:
                    raise ArithmeticError("Matrix instances should have matching dimensions for this operation.")
        except:
            raise  AttributeError("An issue occurred, potential corruption of the Matrix object beforehand")
        

    def dot(self, other):
        if not isinstance(other, Vector):
            TypeError("Operand of the multiplication operator should be a Vector")
        if  (self.shape[1] != 1) or (self.shape != other.shape):
            raise ArithmeticError("Vectors must have the same dimension and \
                be represented as 2-column vectors for this operation.")
        try:
            return sum([self.data[i][0] * other.data[i][0] for i in range(self.shape[0])])
        except:
            raise  AttributeError("An issue occurred, potential corruption of the Matrix object beforehand")
    
    def __str__(self):
        return self.__repr__()


    def __repr__(self):
        try:
            return f"""Vector([{', '.join([str(line) for line in self.data])}])"""
        except:
            raise AttributeError("An issue occurred, potential corruption.")
    
if __name__=='__main__':
    m = Matrix([[1,2,3],[4,5,6]])
    v = Vector([[1],[2],[3],[4],[5],[6]])
    print(m.__str__())
    print(v.__str__())