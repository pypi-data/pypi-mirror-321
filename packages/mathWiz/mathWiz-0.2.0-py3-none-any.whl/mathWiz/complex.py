from typing_extensions import TypeAlias, SupportsFloat, SupportsIndex, Union
import math
import numpy 

_SupportsFloatOrIndex: TypeAlias = SupportsFloat | SupportsIndex

# Complex Number Class

class Complex:
    def __init__(self, real: _SupportsFloatOrIndex, imag: _SupportsFloatOrIndex) -> None:
        self.real = real
        self.imag = imag
    
    def __radd__(self, other):
        return self.__add__(other)
    
    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real + other.real, self.imag + other.imag)
        elif isinstance(other, (int, float)):
            return Complex(self.real + other, self.imag)
        
    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            return Complex(other - self.real, self.imag)
        elif isinstance(other, Complex):
            return other.__sub__(self)
        else:
            return NotImplemented
    
    def __sub__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real - other.real, self.imag - other.imag)
        elif isinstance(other, (int, float)):
            return Complex(self.real - other, self.imag)
        else:
            return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Complex(other*self.real, other*self.imag)
        elif isinstance(other, Complex):
            return Complex(self.real*other.real - self.imag*other.imag, self.real*other.imag + self.imag*other.real)
        else:
            return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, Complex):
            denom = other.real**2 + other.imag**2
            return Complex((self.real * other.real + self.imag * other.imag) / denom,
                           (self.imag * other.real - self.real * other.imag) / denom)
        elif isinstance(other, (int, float)):
            return Complex(self.real / other, self.imag / other)
        else:
            return NotImplemented

    def __rtruediv__(self, other):
        if isinstance(other, (int, float)):
            denom = self.real**2 + self.imag**2
            return Complex((other * self.real) / denom, (-other * self.imag) / denom)
        else:
            return NotImplemented

    def __pow__(self, other):
        if isinstance(other, int):
            result = Complex(1, 0)
            base = Complex(self.real, self.imag)
            exp = other
            if exp == 0:
                return (Complex(1, 0))
            elif exp > 0:
                for _ in range(exp):
                    result *= base
            else:
                base = Complex(1, 0) / base
                exp = -exp
                for _ in range(exp):
                    result *= base
            return result
        else:
            return NotImplemented

    
    def conjugate(self) -> "Complex":
        return Complex(self.real, -self.imag)
    
    def polarForm(self) -> str:
        r = math.sqrt(self.real**2 + self.imag**2)
        theta = math.atan(self.imag/self.real)
        return f"{r}cis({theta})"
    
    def __str__(self) -> str:
        if self.real != 0 and self.imag != 0:
            return f"{self.real} {"+" if self.imag >= 0 else "-"} {abs(self.imag)}i"
        elif self.real != 0:
            return f"{self.real}"
        elif self.imag != 0:
            return f"{self.imag}i"
        return ""