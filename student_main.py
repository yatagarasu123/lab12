class Matrix:
    def __init__(self, rows, columns, data=None):
        self.rows = rows
        self.columns = columns
        if data is None:
            self.data = [[0] * columns for _ in range(rows)]
        else:
            self.data = data

    def add_element(self, row, column, value):
        if 0 <= row < self.rows and 0 <= column < self.columns:
            self.data[row][column] = value
        else:
            print("Invalid position.")

    def sum_of_rows(self):
        return [sum(self.data[row]) for row in range(self.rows)]

    def transpose(self):
        transposed_data = [[self.data[j][i] for j in range(self.rows)] for i in range(self.columns)]
        return Matrix(self.columns, self.rows, transposed_data)

    def multiply_by(self, other):
        if self.columns != other.rows:
            print("Cannot multiply matrices: incompatible dimensions.")
            return None

        result = Matrix(self.rows, other.columns)
        for i in range(self.rows):
            for j in range(other.columns):
                for k in range(self.columns):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]
        return result

    def is_symmetric(self):
        return self.data == self.transpose().data

    def rotate_right(self):
        rotated_data = [[self.data[self.rows - 1 - j][i] for j in range(self.rows)] for i in range(self.columns)]
        self.data = rotated_data
        self.rows, self.columns = self.columns, self.rows

    def flatten(self):
        return [element for row in self.data for element in row]

    @staticmethod
    def from_list(list_of_lists):
        rows = len(list_of_lists)
        columns = len(list_of_lists[0])
        matrix = Matrix(rows, columns)
        for i in range(rows):
            for j in range(columns):
                matrix.data[i][j] = list_of_lists[i][j]
        return matrix

    def diagonal(self):
        if self.rows != self.columns:
            print("Matrix must be square.")
            return None
        return [self.data[i][i] for i in range(self.rows)]

# Example usage
matrix = Matrix(2, 3)
print(matrix.data)  # [[0, 0, 0], [0, 0, 0]]

matrix.add_element(1, 2, 10)
print(matrix.data)  # [[0, 0, 10], [0, 0, 0]]

matrix.add_element(0, 0, 5)
matrix.add_element(0, 1, 10)
matrix.add_element(1, 2, 20)
print(matrix.sum_of_rows())  # [15, 20, 0]

matrix = Matrix(2,3)
matrix.add_element(0, 1, 1)
matrix.add_element(1, 2, 2)
transposed = matrix.transpose()
print(transposed.data)  # [[5, 0], [10, 0], [0, 20]]

matrix1 = Matrix(2, 3)
matrix1.add_element(0, 0, 1)
matrix1.add_element(0, 1, 2)
matrix1.add_element(0, 2, 3)

matrix2 = Matrix(3, 2)
matrix2.add_element(0, 0, 1)
matrix2.add_element(1, 0, 2)
matrix2.add_element(2, 0, 3)

result = matrix1.multiply_by(matrix2)
print(result.data)  # [[14, 0], [0, 0]]

matrix = Matrix(2, 2)
matrix.add_element(0, 1, 5)
matrix.add_element(1, 0, 5)
print(matrix.is_symmetric())  # True

matrix = Matrix(2, 2)
matrix.add_element(0, 0, 1)
matrix.add_element(0, 1, 2)
matrix.add_element(1, 0, 3)
matrix.add_element(1, 1, 4)
matrix.rotate_right()
print(matrix.data)  # [[3, 1], [4, 2]]

matrix = Matrix(2, 2)
matrix.add_element(0, 0, 1)
matrix.add_element(0, 1, 2)
matrix.add_element(1, 0, 3)
matrix.add_element(1, 1, 4)
print(matrix.flatten())  # [1, 2, 3, 4]

list_of_lists = [[1, 2], [3, 4]]
matrix = Matrix.from_list(list_of_lists)
print(matrix.data) # [[1, 2], [3, 4]]

matrix = Matrix(3, 3)
matrix.add_element(0, 0, 1)
matrix.add_element(1, 1, 2)
matrix.add_element(2, 2, 3)
print(matrix.diagonal())  # [1, 2, 3]