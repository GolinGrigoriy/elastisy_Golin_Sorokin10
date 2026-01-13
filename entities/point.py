from dataclasses import dataclass
from typing import Callable, Optional
import numpy as np


@dataclass
class Point:
    """Пространственная точка в 2D"""
    x: float
    y: float

    def __add__(self, other: 'Point') -> 'Point':
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar: float) -> 'Point':
        return Point(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar: float) -> 'Point':
        return self.__mul__(scalar)

    def as_array(self) -> np.ndarray:
        return np.array([self.x, self.y])

    @classmethod
    def from_array(cls, arr: np.ndarray) -> 'Point':
        return cls(arr[0], arr[1])