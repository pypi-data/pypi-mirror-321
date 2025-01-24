import math
from typing import *

from numpy import *
from numpy.ma.core import arccos

from pryttier.tools import isDivisibleBy

PI = 2 * arccos(0)
Degrees = PI / 180


def summation(n: float | int, i: float | int, expr: Callable) -> float:
    total = 0
    for j in range(n, i + 1):
        total += expr(j)
    return total


def product(n: int, i: int, expr: Callable) -> float:
    total = 1
    for j in range(n, i):
        total *= expr(j)
    return total


def clamp(num: float, low: float, high: float) -> float:
    if num < low:
        return low
    if num > high:
        return high
    return num


def sign(num: float) -> int:
    return int(num / abs(num))


def factorial(num: int) -> int:
    if num == 0:
        return 1
    if num == 1:
        return 1
    return num * factorial(num - 1)


def binToDec(num: int) -> int:
    digits = [int(i) for i in list(str(num))]
    total = 0
    for j in range(0, len(digits)):
        total += (2 ** j) * (digits[j])
    return total


def mapRange(value: int | float,
             min1: float,
             max1: float,
             min2: float,
             max2: float) -> float:
    return (value - min1) / (max1 - min1) * (max2 - min2) + min2


def isPrime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def getFactors(num: int):
    factors = []
    for i in range(1, num + 1):
        if num | isDivisibleBy | i:
            factors.append(i)

    return factors


def radToDeg(num: float):
    return num * (180 / PI)


def degToRad(num: float):
    return num * (PI / 180)


class Vector2:
    def __init__(self,
                 x: float | int,
                 y: float | int):
        self.x = x
        self.y = y
        self.magnitude = sqrt(self.x * self.x + self.y * self.y)

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

    def __add__(self, other: Self) -> Self:
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Self) -> Self:
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Self | float | int) -> Self:
        if isinstance(other, float) or isinstance(other, int):
            return Vector2(self.x * other, self.y * other)
        elif isinstance(other, Vector2):
            return Vector2(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return Vector2(self.x / other, self.y / other)
        elif isinstance(other, Vector2):
            return Vector2(self.x / other.x, self.y / other.y)

    def __iter__(self):
        return iter([self.x, self.y])

    def normalize(self) -> Self:
        return Vector2(self.x / self.magnitude, self.y / self.magnitude)

    def toInt(self):
        return Vector2(int(self.x), int(self.y))

    # ---Class Methods---
    @classmethod
    def distance(cls, a: Self, b: Self):
        dx = b.x - a.x
        dy = b.y - a.y
        return math.sqrt(dx * dx + dy * dy)

    @classmethod
    def dot(cls, a: Self, b: Self):
        return a.x * b.x + a.y * b.y

    @classmethod
    def cross(cls, a: Self, b: Self):
        return a.x * b.y - a.y * b.x

    @classmethod
    def angleBetween(cls, a: Self, b: Self):
        dotProduct = cls.dot(a, b)
        magA = a.magnitude
        magB = b.magnitude
        return math.acos(dotProduct / (magA * magB))

    @classmethod
    def interpolate(cls, a: Self, b: Self, t: float):
        v = b - a
        pdx = a.x + v.x * t
        pdy = a.y + v.y * t
        return Vector2(pdx, pdy)

class Vector3:
    def __init__(self,
                 x: float | int,
                 y: float | int,
                 z: float | int):
        self.x = x
        self.y = y
        self.z = z
        self.magnitude = sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def __repr__(self) -> str:
        return f"({self.x}, {self.y}, {self.z})"

    def __add__(self, other: Self) -> Self:
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: Self) -> Self:
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other: Self | float | int) -> Self:
        if isinstance(other, float) or isinstance(other, int):
            return Vector3(self.x * other, self.y * other, self.z * other)
        elif isinstance(other, Vector3):
            return Vector3(self.x * other.x, self.y * other.y, self.z * other.z)

    def __truediv__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return Vector3(self.x / other, self.y / other, self.z / other)
        elif isinstance(other, Vector3):
            return Vector3(self.x / other.x, self.y / other.y, self.z / other.z)

    def __iter__(self):
        return iter([self.x, self.y, self.z])

    def normalize(self) -> Self:
        return Vector3(self.x / self.magnitude, self.y / self.magnitude, self.z / self.magnitude)

    def toInt(self):
        return Vector3(int(self.x), int(self.y), int(self.z))
    # ---Class Methods---
    @classmethod
    def distance(cls, a: Self, b: Self):
        dx = b.x - a.x
        dy = b.y - a.y
        dz = b.z - a.z
        return math.sqrt(dx * dx + dy * dy + dz * dz)

    @classmethod
    def dot(cls, a: Self, b: Self):
        return a.x * b.x + a.y * b.y + a.z * a.z

    @classmethod
    def cross(cls, a: Self, b: Self) -> Self:
        i = a.y * b.z - a.z * b.y
        j = a.z * b.x - a.x * b.z
        k = a.x * b.y - a.y * b.x
        return Vector3(i, j, k)

    @classmethod
    def angleBetween(cls, a: Self, b: Self):
        dotProduct = cls.dot(a, b)
        magA = a.magnitude
        magB = b.magnitude
        return math.acos(dotProduct / (magA * magB))


    @classmethod
    def interpolate(cls, a: Self, b: Self, t: float):
        v = b - a
        pdx = a.x + v.x * t
        pdy = a.y + v.y * t
        pdz = a.z + v.z * t
        return Vector3(pdx, pdy, pdz)

class Matrix:
    def __init__(self, mat: Sequence[Sequence[int | float]]):
        self.matrix = array(mat)
        self.rows = len(self.matrix)
        self.cols = len(self.matrix[0])
        self.size = (self.rows, self.cols)

    def __repr__(self):
        return str(self.matrix)

    def __neg__(self):
        mat = []
        for i in self.matrix:
            mat.append([])
            for a in i:
                mat[-1].append(-a)
        return Matrix(mat)

    def __add__(self, other: Self):
        if self.size != other.size:
            raise ValueError(f"Cannot add matrices with sizes {self.size}, {other.size}")
        mat = []
        for i, j in zip(self.matrix, other.matrix):
            mat.append([])
            for a, b in zip(i, j):
                mat[-1].append(a + b)
        return Matrix(mat)

    def __sub__(self, other: Self):
        return self + -other

    def __mul__(self, other: Self | int | float):
        if isinstance(other, int) or isinstance(other, float):
            mat = []
            for i in self.matrix:
                mat.append([])
                for a in i:
                    mat[-1].append(a * other)
            return Matrix(mat)
        if isinstance(other, Matrix):
            a = self.matrix
            b = other.matrix

            if self.cols != other.rows:
                raise ValueError(
                    f"Number of columns of the first matrix (cols: {self.cols}) must be equal to the number of rows of the second matrix (rows: {other.rows})")

            result = dot(a, b)

            return Matrix(result)

    def swapColsAndRows(self):
        mat = [[self.matrix[i][j] for i in range(self.rows)] for j in range(self.cols)]
        return Matrix(mat)
