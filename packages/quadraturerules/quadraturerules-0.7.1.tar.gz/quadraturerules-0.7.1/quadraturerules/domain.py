"""Integral domains."""

from enum import Enum


class Domain(Enum):
    """A domain of an integral."""

    EdgeAdjacentTriangleAndQuadrilateral = 0
    Interval = 1
    Quadrilateral = 2
    TriangularPrism = 3
    VertexAdjacentTriangles = 4
    VertexAdjacentTriangleAndQuadrilateral = 5
    SquareBasedPyramid = 6
    Triangle = 7
    Hexahedron = 8
    Tetrahedron = 9
    EdgeAdjacentTriangles = 10
    EdgeAdjacentQuadrilaterals = 11
    VertexAdjacentQuadrilaterals = 12
