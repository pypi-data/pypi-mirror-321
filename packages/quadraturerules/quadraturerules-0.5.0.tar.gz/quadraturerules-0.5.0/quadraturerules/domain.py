"""Integral domains."""

from enum import Enum


class Domain(Enum):
    """A domain of an integral."""

    Interval = 0
    Hexahedron = 1
    Tetrahedron = 2
    Quadrilateral = 3
    TriangularPrism = 4
    Triangle = 5
    SquareBasedPyramid = 6
