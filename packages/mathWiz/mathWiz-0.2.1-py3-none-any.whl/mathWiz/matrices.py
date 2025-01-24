from typing_extensions import TypeAlias, SupportsFloat, SupportsIndex, Union
import math
import numpy 

_SupportsFloatOrIndex: TypeAlias = SupportsFloat | SupportsIndex

# Matrices

class Matrix:
    def __init__(self, matrix: list[list[_SupportsFloatOrIndex]]):
        self.matrix = matrix
        self.rows: int = len(matrix)
        self.columns: int = len(matrix[0])

        self._maxColumnLengths = []
        self._actualColumns = []
        
        for i in range(self.columns):
            actualColumn = []
            for j in range(self.rows):
                actualColumn.append(round(self.matrix[j][i], 2))
            self._actualColumns.append(actualColumn)

        for i in range(self.rows):
            for j in range(self.columns):
                maxColumnLength = max(len(x) for x in (str(x) for x in self._actualColumns[j]))
                self._maxColumnLengths.append(maxColumnLength)
    
    def __radd__(self, other):
        return self.__add__(other)
    
    def __add__(self, other):
        if isinstance(other, Matrix):
            if other.rows == self.rows and other.columns == self.columns:
                newMatrix = []
                for i in range(self.rows):
                    row = []
                    for j in range(self.columns):
                        row.append(self.matrix[i][j] + other.matrix[i][j])
                    newMatrix.append(row)

                return Matrix(newMatrix)
                        
            else:
                raise Exception("The addition of two matrix's require them to have the same dimensions")
        else:
            raise TypeError("Object of not type Matrix is trying to be added to a Matrix")

    def __rsub__(self, other):
        if isinstance(other, Matrix):
            if other.rows == self.rows and other.columns == self.columns:
                newMatrix = []
                for i in range(self.rows):
                    row = []
                    for j in range(self.columns):
                        row.append(other.matrix[i][j] - self.matrix[i][j])
                    newMatrix.append(row)

                return Matrix(newMatrix)
            else:
                raise Exception("The subtraction of two matrix's require them to have the same dimensions")
        else:
            raise TypeError("Object of not type Matrix is trying to be subtracte from a Matrix")
    
    def __sub__(self, other):
        if isinstance(other, Matrix):
            if other.rows == self.rows and other.columns == self.columns:
                newMatrix = []
                for i in range(self.rows):
                    row = []
                    for j in range(self.columns):
                        row.append(self.matrix[i][j] - other.matrix[i][j])
                    newMatrix.append(row)

                return Matrix(newMatrix)
            else:
                raise Exception("The subtraction of two matrix's require them to have the same dimensions")
        else:
            raise TypeError("Object of not type Matrix is trying to be subtracte from a Matrix")

    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            resultingMatrix = [[other*element for element in row] for row in self.matrix]
            return Matrix(resultingMatrix)
        elif isinstance(other, Matrix):
            if self.columns == other.rows or other.columns == self.rows:
                result = [[0 for _ in range(other.columns)] for _ in range(self.rows)]

                for i in range(self.rows):
                    for j in range(other.columns):
                        for k in range(other.rows):
                            result[i][j] += self.matrix[i][k] * other.matrix[k][j]
                
                return Matrix(result)
            else:
                raise Exception("Matrix Multiplication requires the rows of one matrix to be equal to the columns of the other: Invalid Matrix Dimensions ")
        else:
            raise TypeError("Matrix's can only be multiplied by int/float scalars, or other Matrix's")

    def determinant(self) -> float:
        if self.rows == self.columns:
            if len(self.matrix) == 2:
                return self.matrix[0][0] * self.matrix[1][1] - self.matrix[1][0] * self.matrix[0][1]
            det = 0 
            for col in range(len(self.matrix)): 
                submatrix = [row[:col] + row[col + 1:] for row in self.matrix[1:]] 
                sign = (-1) ** col 
                sub_det = Matrix(submatrix).determinant()
                det += sign * self.matrix[0][col] * sub_det 

            return det  
        
        return None
    
    def transpose(self) -> "Matrix":
        newMatrix = []
        for i in range(self.columns):
            column = []
            for j in range(self.rows):
                column.append(self.matrix[j][i])
            newMatrix.append(column)
        return Matrix(newMatrix)

    def cofactorMatrix(self) -> "Matrix":
        if self.rows == 2:
            co_matrix = [[self.matrix[1][1], -self.matrix[1][0]], [-self.matrix[0][1], self.matrix[0][0]]]
            return Matrix(co_matrix)
        else:
            co_matrix = [[0 for _ in range(self.columns)] for _ in range(self.rows)]
            for i in range(self.rows):
                for j in range(self.columns):
                    submatrix = [row[:j] + row[j + 1:] for row in (self.matrix[:i] + self.matrix[i + 1:])]
                    subMatrix = Matrix(submatrix)
                    co_matrix[i][j] = ((-1)**(i+j+2))*(subMatrix.determinant())
            return co_matrix    

    def adjointMatrix(self) -> "Matrix":
        return self.cofactorMatrix().transpose()

    def inverse(self) -> "Matrix":
        if self.rows == self.columns:
            det = self.determinant()
            if det != 0:
                if self.rows == 2:
                    adjmatrix = [[self.matrix[1][1], -self.matrix[0][1]], [-self.matrix[1][0], self.matrix[0][0]]]
                    return Matrix(adjmatrix) * (1/det)
                else:
                    adjmatrix = [[0 for _ in range(self.columns)] for _ in range(self.rows)]
                    for i in range(self.rows):
                        for j in range(self.columns):
                            submatrix = [row[:j] + row[j + 1:] for row in (self.matrix[:i] + self.matrix[i + 1:])]
                            subMatrix = Matrix(submatrix)
                            adjmatrix[i][j] = ((-1)**(i+j+2))*(subMatrix.determinant())
                    
                    adjMatrix = Matrix(adjmatrix).transpose()
                    return adjMatrix * (1/det)
            
        return None
    
    def __str__(self):
        string = f' _{(sum(self._maxColumnLengths[:self.columns])+2*self.columns-2)*" "}_\n'
        for i in range(self.rows):
            string += '|'
            if i == self.rows - 1:
                string += "_"
            for j in range(self.columns):
                maxColumnLength = max(len(x) for x in (str(x) for x in self._actualColumns[j]))
                string += f"{" "*(maxColumnLength-len(str(round(self.matrix[i][j], 2))))}{"" if i == self.rows - 1 and j == 0 else " "}{round(self.matrix[i][j], 2)}{"" if i == self.rows - 1 and j == self.columns - 1 else " "}"
            string += f'{'_' if i == self.rows - 1 else ""}|\n'
        return string