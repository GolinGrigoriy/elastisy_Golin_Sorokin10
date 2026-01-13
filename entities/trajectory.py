from typing import List, Tuple
from dataclasses import dataclass
from .point import Point
import numpy as np


@dataclass
class Trajectory:
    """Траектория движения материальной точки"""
    points: List[Point]
    times: List[float]

    def get_coordinates(self) -> Tuple[np.ndarray, np.ndarray]:
        """Возвращает массивы x и y координат"""
        x_vals = [p.x for p in self.points]
        y_vals = [p.y for p in self.points]
        return np.array(x_vals), np.array(y_vals)

    def get_last_point(self) -> Point:
        """Возвращает последнюю точку траектории"""
        return self.points[-1]