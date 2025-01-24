from typing_extensions import TypeAlias, SupportsFloat, SupportsIndex, Union
import math
import numpy 

_SupportsFloatOrIndex: TypeAlias = SupportsFloat | SupportsIndex

# 2D Vector
#TODO: Add vector addition and subtraction
class Vector2:
    def __init__(self, i: _SupportsFloatOrIndex, j: _SupportsFloatOrIndex) -> None:
        self.i = i
        self.j = j

        self.magnitude = math.sqrt(self.i**2 + self.j**2)
        self.direction = math.atan(self.j/self.i)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector2(round(self.i * other, 4), round(self.j * other, 4))
        else:
            return NotImplemented
    
    def unitVector(self) -> "Vector2":
        return (1/self.magnitude) * self

    def __str__(self):
        return f"({round(self.i, 4)}, {round(self.j, 4)})"

# 3D Vector
#TODO: IMPLEMENT further vector functions (e.g. vector equation of a line) in future versions
class Vector3:
    def __init__(self, i: _SupportsFloatOrIndex, j: _SupportsFloatOrIndex, k: _SupportsFloatOrIndex) -> None:
        self.i = i
        self.j = j
        self.k = k

        self.magnitude = math.sqrt(self.i**2 + self.j**2 + self.k**2)
        self.direction = [math.atan(self.j/self.i), math.acos(self.k / self.magnitude)]

    def __rmul__(self, other):
        return self.__mul__(other)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector3(round(self.i * other, 4), round(self.j * other, 4), round(self.k * other, 4))
        elif isinstance(other, Vector3):
            return Vector3(self.j * other.k - self.k * other.j, self.k * other.i - self.i * other.k, self.i * other.j - self.j * other.i)
    
    def unitVector(self) -> "Vector3":
        return (1/self.magnitude) * self
    
    def __str__(self):
        return f"({round(self.i, 4)}, {round(self.j, 4)}, {round(self.k, 4)})"


def dotProduct(vectorA: Union[Vector2, Vector3], vectorB: Union[Vector2, Vector3]) -> float:
    if type(vectorA) == type(vectorB) and (type(vectorB) == Vector2 or type(vectorB) == Vector3):
        if type(vectorA) == Vector2:
            return vectorA.i*vectorB.i + vectorA.j*vectorB.j
        else:
            return vectorA.i*vectorB.i + vectorA.j*vectorB.j + vectorA.k*vectorB.k
    else:
        raise TypeError("Only vectors of the same type are valid inputs")

def scalarProjection(vectorA: Union[Vector2, Vector3], vectorB: Union[Vector2, Vector3]):
    if type(vectorA) == type(vectorB) and (type(vectorB) == Vector2 or type(vectorB) == Vector3):
        return dotProduct(vectorA, vectorB.unitVector())
    else:
        raise TypeError("Only vectors of the same type are valid inputs")
    
def vectorProjection(vectorA: Union[Vector2, Vector3], vectorB: Union[Vector2, Vector3]):
    if type(vectorA) == type(vectorB) and (type(vectorB) == Vector2 or type(vectorB) == Vector3):
        return (dotProduct(vectorA, vectorB) * (1 / dotProduct(vectorB, vectorB))) * vectorB
    else:
        raise TypeError("Only vectors of the same type are valid inputs")