"""Integral domains."""

from enum import Enum


class Domain(Enum):
    """A domain of an integral."""

    SquareBasedPyramid = 0
    Triangle = 1
    Quadrilateral = 2
    Hexahedron = 3
    Interval = 4
    TriangularPrism = 5
    Tetrahedron = 6
