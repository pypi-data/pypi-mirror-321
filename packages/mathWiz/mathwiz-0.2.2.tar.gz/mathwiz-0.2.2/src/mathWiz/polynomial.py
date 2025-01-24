from typing_extensions import TypeAlias, SupportsFloat, SupportsIndex, Union
import math
import numpy 
from complex import Complex

_SupportsFloatOrIndex: TypeAlias = SupportsFloat | SupportsIndex

# Point

class Point:
    def __init__(self, x: _SupportsFloatOrIndex, y: _SupportsFloatOrIndex):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self): 
        return self.__str__()
    
# Polynomials

class Variable:
    def __init__(self, symbol : str) -> None:
        self.symbol = symbol
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Term(self, other > 0, other, 1)
        elif isinstance(other, Term):
            return Term(self, other.positive, other.coefficient, other.power + 1)
    
    def __pow__(self, power):
        if isinstance(power, (int, float)):
            return Term(self, True, 1, power)

class Term:
    def __init__(self, variable : Variable, positive : bool, coefficient : float, power : float) -> None:
        self.variable = variable
        self.positive = positive
        self.coefficient = coefficient
        self.power = power

    def __radd__(self, other):
        return self.__add__(other)

    def _rsub__(self, other):
        return self.__sub__(other)

    def __add__(self, other):
        if isinstance(other, Term):
            return Expression([self, other])
        elif isinstance(other, Variable):
            return Expression([self, Term(self.variable, True, 1, 1)])
        elif isinstance(other, (int, float)):
            return Expression([self, Term(self.variable, other > 0, other, 0)])
        elif isinstance(other, Expression):
            return Expression(other.terms + [self])
    
    def __sub__(self, other):
        if isinstance(other, Term):
            return Expression([self, Term(other.variable, False if other.positive else True, other.coefficient, other.power)])
        elif isinstance(other, Variable):
            return Expression(self, Term(self.variable, False, -1, 1))
        elif isinstance(other, (int, float)):
            return Expression([self, Term(self.variable, False, -other, 0)])
        elif isinstance(other, Expression):
            return Expression(other.terms + [self])
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Term(self.variable, self.coefficient * other > 0, self.coefficient * other, self.power)
    
    def __pow__(self, other):
        if isinstance(other, (int, float)):
            return Term(self.variable, self.coefficient ** other > 0, self.coefficient ** other, self.power * other)
    
    def __str__(self):
        if self.coefficient != 1:
            if self.power == 1:
                return f"{abs(self.coefficient)}{self.variable.symbol}"
            elif self.power == 0:
                return f"{abs(self.coefficient)}"
            else:
                return f"{abs(self.coefficient)}{self.variable.symbol}^{self.power}"
        else:
            if self.power == 1:
                return f"{self.variable.symbol}"
            elif self.power == 0:
                return f"{1}"
            else:
                return f"{self.variable.symbol}^{self.power}"

class Expression:
    def __init__(self, terms : list[Term]) -> None:
        self.terms = terms
    
    def __radd__(self, other):
        return self.__add__(other)
    
    def __add__(self, other):
        if isinstance(other, (int, float)):
            return Expression(self.terms + [Term(self.terms[0].variable, other > 0, other, 0)])
        elif isinstance(other, (Term)):
            return Expression(self.terms + [other])

    def __rsub__(self, other):
        return self.__sub__(other)
    
    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return Expression(self.terms + [Term(self.terms[0].variable, False, other, 0)])
        elif isinstance(other, (Term)):
            return Expression(self.terms + [Term(other.variable, False, other.coefficient, other.power)])

class Polynomial:
    def __init__(self, degree, expression : Expression):
        self.degree = degree
        self.expression = expression
    
    def subIn(self, x: _SupportsFloatOrIndex, complex = False) -> float:
        if complex == False:
            value = 0
            for term in self.expression.terms:
                if term.positive:
                    value += (term.coefficient*(x**term.power))
                else:
                    value -= (term.coefficient*(x**term.power))
        else:
            value = Complex(0,0)
            for term in self.expression.terms:
                if term.positive:
                    value += (term.coefficient*(x**term.power))
                else:
                    value -= (term.coefficient*(x**term.power))
        return value

    def roots(self) -> list[Point]:
        roots = []
        coefficients = []
        sorted(self.expression.terms, key= lambda t: -t.power)
        for term in self.expression.terms:
            while (self.degree - len(coefficients) > term.power):
                coefficients.append(0)

            if term.positive == False:
                coefficients.append(-term.coefficient)
            else:
                coefficients.append(term.coefficient)
        while (self.degree - len(coefficients) + 1 > 0):
            coefficients.append(0)
        npRoots = numpy.roots(coefficients)
        for root in npRoots:
            if type(root) == numpy.float64:
                roots.append(Point(root, 0)) 
            else:
                roots.append(Point(Complex(root.real, root.imag), 0))
                
        return roots

    def turningPoints(self) -> list[Point]:
        derivativePolynomial = self.derivative()
        points: list[Point] = derivativePolynomial.roots() 
        turnPoints = []
        for point in points:
            turnPoints.append(Point(point.x, self.subIn(point.x)))
        return turnPoints

    def derivative(self) -> "Polynomial":
        newTerms = []
        for term in self.expression.terms:
            if term.power != 0:
                newTerm = Term(term.variable, term.positive, term.coefficient*term.power, term.power - 1)
                newTerms.append(newTerm)

        derivedPolynomial = Polynomial(self.degree - 1, Expression(newTerms))
        return derivedPolynomial

    def gradientAt(self, x: _SupportsFloatOrIndex) -> float:
        derivativePolynomial = self.derivative()
        return derivativePolynomial.subIn(x)

    def integral(self) -> "Polynomial":
        newTerms = []
        for term in self.expression.terms:
            newTerm = Term(term.variable, term.positive, term.coefficient/(term.power+1), term.power + 1)
            newTerms.append(newTerm)
        
        integratedPolynomial = Polynomial(self.degree + 1, Expression(newTerms))
        return integratedPolynomial
    
    def definiteIntegral(self, lowerBound: _SupportsFloatOrIndex, upperBound: _SupportsFloatOrIndex) -> float:
        integratedPolynomial = self.integral()
        return integratedPolynomial.subIn(upperBound) - integratedPolynomial.subIn(lowerBound)

    def __str__(self) -> str:
        string = ""
        for term in self.expression.terms:
            if self.expression.terms.index(term) == 0:
                if term.positive == False:
                    string += "-"
            else:
                string += f'{" + " if term.positive else " - "}'
            string += term.__str__()
        return string