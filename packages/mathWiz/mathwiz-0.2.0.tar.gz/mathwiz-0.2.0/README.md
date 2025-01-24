# MathWiz

## Description

MathWiz is a Python library that was written in Python. It is specifically designed for use in various aspects of mathematics, as per listed below. Other common python math modules such as numpy provide similiar (overlapping) services, however there are many unique advantages and processes offered by this module.

## Installation

The module mathWiz is available to __install via pip__:

```sh
pip install mathWiz
```

Use the following command to upgrade to the most recent version (__Recommended__ due to bug fixes and new features)
```sh
pip install --upgrade mathWiz
```

## Version

MathWiz is currently on version 0.2.0

#### Latest Additions

- Simultaneous Equations:
    - Solving of any order

- Matrices:
    - Adjoint Matrix Function
    - Cofactor Matrix Function

See Changelogs in (CHANELOG.md) for more information

## Features

#### Complex Numbers

- Operations
- Conjugates
- Polar Form

#### Polynomials

- Roots
- Turning Points
- Substitution (Real and Complex)
- Derivatives
- Gradient
- Integrals
- Area Under Curve

#### Matrices

- Addition and Subtraction
- Multiplication
- Determinants
- Transposition
- Adjoint Matrix Function
- Cofactor Matrix Function
- Inverse Matrices

#### Simulataneous Equations

- Solving with any amount of variables

#### Vectors

- 2D Vectors
- 3D Vectors
- Unit Vectors
- Scalar Multiplication
- Dot Products
- Cross Multiplication
- Scalar Projection
- Vector Projection

More Features will be coming soon

## Usage / Documentation

Here are some examples on how you can use the above mentioned features with mathWiz.


#### Complex Numbers

```python
z = Complex(3, 4)

z
# 3 + 4i

z.conjugate()
# 3 - 4i

z.polarForm()
# 5cis(0.9272952180016122)

z + Complex(4,-2)
# 7 + 2i

z * Complex(2, 4)
# -10 + 20i

z ** 5
# -237 - 3116i
```

#### Polynomials

```python
x = Variable('x')
poly = Polynomial(3, 2*x**3 - 4*x**2 + 12)

poly
# 2x^3 - 4x^2 + 12

poly.subIn(2)
# 12

poly.subIn(Complex(2,-3))
# -60 + 30i

poly.roots()
# [(1.670125415064549 + 1.2990208027107955i, 0), (1.670125415064549 - 1.2990208027107955i, 0), (-1.3402508301290976, 0)]

poly.turningPoints()
# [(1.3333333333333333, 9.62962962962963), (0.0, 12.0)]

poly.derivative()
# 6x^2 - 8x

poly.gradientAt(x=4)
# 64

poly.integral()
# 0.5x^4 - 1.33x^3 + 12.0x

poly.definiteIntegral(lowerBound=1, upperBound=3)
# 29.333333333333336
```

#### Matrices

```python
matrix = Matrix([[1,-4.89,5,7], [6,3,2,5], [1,4,3,-2.53], [8,7,3,5]])
matrix2 = Matrix([[2,-3,4,8],[1,1,0,0],[9,2,1,-3.42],[8,1,7,1]])

matrix
"""
 _                  _
| 1  -4.89  5      7 |
| 6      3  2      5 |
| 1      4  3  -2.53 |
|_8      7  3      5_| 
"""
matrix.rows 
# 4

matrix.columns 
# 4

matrix + matrix2
"""
 _                    _
|  3  -7.89   9     15 |
|  7      4   2      5 |
| 10      6   4  -5.95 |
|_16      8  10      6_|
"""

matrix * matrix2
"""
 _                          _
| 98.11  9.11    58.0   -2.1 |
|    73    -6      61  46.16 |
| 12.76  4.47  -10.71  -4.79 |
|_   90    -6      70  58.74_|
"""

matrix.determinant()
# 264.54339999999985

matrix.transpose()
"""
 _                  _
|     1  6      1  8 |
| -4.89  3      4  7 |
|     5  2      3  3 |
|_    7  5  -2.53  5_|
"""

matrix.inverse()
"""
 _                         _
| -0.2   1.37   0.34  -0.92 |
| 0.08  -0.95  -0.22   0.73 |
|  0.1   0.05   0.22  -0.08 |
|_0.15  -0.89  -0.36    0.7_|
"""

matrix.inverse()*matrix
"""
 _                    _
| 1.0  -0.0  0.0   0.0 |
| 0.0   1.0  0.0  -0.0 |
| 0.0   0.0  1.0  -0.0 |
|_0.0   0.0  0.0   1.0_|
"""
```

#### Simultaneous Equations

```python
solveSim('2x+3y-z=7', '-x+4y+2z =1', '3x-5y+z=-8')
# [{'x': 0.36}, {'y': 1.39}, {'z': -2.11}]
```

#### Vectors

```python
vectorL = Vector2(2, 3)

vectorL
# (2, 3)

vectorL.i
# 2

vectorL.j
# 3

vectorL.magnitude 
# 3.605551275463989

vectorL.direction
# 0.982793723247329

vectorL * 3
# (6, 9)

vectorL.unitVector()
# (0.5547, 0.8321)

dotProduct(vectorL, Vector2(1,2))
# 8

vectorA = Vector3(4, 3, -5)
vectorB = Vector3(-5.4, 7, 2)

vectorA.k
# -5

vectorA * vectorB:
# (41, 19.0, 44.2)

scalarProjection(vectorA, vectorB) # vector A on vector B
# -1.1689

vectorProjection(vectorA, vectorB) # vector A on vector B
# (0.6967, -0.9031, -0.258) 
```

## License 

This project is licensed under the MIT License. See the LICENSE file for more details.

## Credits

This module was created by William E.
