from typing import List, Tuple
from dataclasses import dataclass
import numpy as np
from .point import Point
from .trajectory import Trajectory


class MaterialBody:
    """Материальное тело, состоящее из множества точек"""

    def __init__(self, points: List[Point]):
        self.initial_points = points.copy()
        self.current_points = points.copy()
        self.trajectories = [Trajectory([p], [0.0]) for p in points]

    def update_points(self, points: List[Point], time: float):
        """Обновляет положение точек тела и их траектории"""
        self.current_points = points.copy()
        for i, (point, trajectory) in enumerate(zip(points, self.trajectories)):
            trajectory.points.append(point)
            trajectory.times.append(time)

    def get_initial_shape(self) -> Tuple[np.ndarray, np.ndarray]:
        """Возвращает начальную форму тела"""
        x_vals = [p.x for p in self.initial_points]
        y_vals = [p.y for p in self.initial_points]
        return np.array(x_vals), np.array(y_vals)

    def get_current_shape(self) -> Tuple[np.ndarray, np.ndarray]:
        """Возвращает текущую (деформированную) форму тела"""
        x_vals = [p.x for p in self.current_points]
        y_vals = [p.y for p in self.current_points]
        return np.array(x_vals), np.array(y_vals)

    def get_trajectories_data(self) -> List[Tuple[np.ndarray, np.ndarray]]:
        """Возвращает данные всех траекторий"""
        return [traj.get_coordinates() for traj in self.trajectories]

    @staticmethod
    def create_circle_quarter(radius: float, num_points: int = 50) -> 'MaterialBody':
        """Создает тело в форме четверти окружности"""
        points = []
        angles = np.linspace(0, np.pi / 2, num_points)

        for angle in angles:
            x = radius * np.cos(angle)
            y = radius * np.sin(angle)
            points.append(Point(x, y))

        return MaterialBody(points)