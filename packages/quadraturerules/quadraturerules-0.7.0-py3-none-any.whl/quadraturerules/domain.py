"""Integral domains."""

from enum import Enum


class Domain(Enum):
    """A domain of an integral."""

    Triangle = 0
    Tetrahedron = 1
    TriangularPrism = 2
    VertexAdjacentTriangleAndQuadrilateral = 3
    VertexAdjacentTriangles = 4
    Quadrilateral = 5
    EdgeAdjacentTriangleAndQuadrilateral = 6
    Hexahedron = 7
    SquareBasedPyramid = 8
    VertexAdjacentQuadrilaterals = 9
    EdgeAdjacentTriangles = 10
    Interval = 11
    EdgeAdjacentQuadrilaterals = 12
