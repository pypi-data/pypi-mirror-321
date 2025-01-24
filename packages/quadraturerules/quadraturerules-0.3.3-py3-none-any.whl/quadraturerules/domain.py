"""Integral domains."""

from enum import Enum


class Domain(Enum):
    """A domain of an integral."""

    Triangle = 0
    Tetrahedron = 1
    Interval = 2
