class Matrix:
    def __init__(self, data):
        self.data = data
    def __matmul__(self, other):
        a = self.data
        b = other.data
        return Matrix([
            [a[0][0] * b[0][0] + a[0][1] * b[1][0],
             a[0][0] * b[0][1] + a[0][1] * b[1][1]],
            [a[1][0] * b[0][0] + a[1][1] * b[1][0],
             a[1][0] * b[0][1] + a[1][1] * b[1][1]]
        ])
a = Matrix([[1, 2], [3, 4]])
b = Matrix([[5, 6], [7, 8]])
a @= b
print(a.data)
