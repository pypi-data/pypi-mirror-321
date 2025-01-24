"""Integral domains."""

from enum import Enum


class Domain(Enum):
    """A domain of an integral."""

    Hexahedron = 0
    SquareBasedPyramid = 1
    Tetrahedron = 2
    Quadrilateral = 3
    Triangle = 4
    Interval = 5
    TriangularPrism = 6
