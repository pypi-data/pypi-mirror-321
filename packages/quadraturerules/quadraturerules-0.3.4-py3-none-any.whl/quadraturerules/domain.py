"""Integral domains."""

from enum import Enum


class Domain(Enum):
    """A domain of an integral."""

    Interval = 0
    Tetrahedron = 1
    Triangle = 2
