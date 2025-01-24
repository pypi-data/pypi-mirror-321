"""Integral domains."""

from enum import Enum


class Domain(Enum):
    """A domain of an integral."""

    Interval = 0
    Triangle = 1
    Tetrahedron = 2
