"""Integral domains."""

from enum import Enum


class Domain(Enum):
    """A domain of an integral."""

    Triangle = 0
    Interval = 1
    Tetrahedron = 2
