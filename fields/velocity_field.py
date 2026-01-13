from typing import Callable, Tuple
import numpy as np
from entities.point import Point


class VelocityField:
    """Поле скоростей v1 = -A(t)x1, v2 = B(t)x2"""

    def __init__(self, A_func: Callable[[float], float],
                 B_func: Callable[[float], float]):
        self.A_func = A_func
        self.B_func = B_func

    def get_velocity(self, point: Point, time: float) -> Point:
        """Возвращает скорость в данной точке в заданный момент времени"""
        v_x = -self.A_func(time) * point.x
        v_y = self.B_func(time) * point.y
        return Point(v_x, v_y)

    def get_velocity_func(self) -> Callable[[float, np.ndarray], np.ndarray]:
        """Возвращает функцию для решателя ОДУ"""

        def func(t: float, y: np.ndarray) -> np.ndarray:
            point = Point.from_array(y)
            velocity = self.get_velocity(point, t)
            return velocity.as_array()

        return func

    def generate_streamlines(self, x_range: Tuple[float, float],
                             y_range: Tuple[float, float],
                             time: float,
                             grid_size: int = 20) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        """Генерирует линии тока для визуализации"""
        x = np.linspace(x_range[0], x_range[1], grid_size)
        y = np.linspace(y_range[0], y_range[1], grid_size)
        X, Y = np.meshgrid(x, y)

        U = np.zeros_like(X)
        V = np.zeros_like(Y)

        for i in range(grid_size):
            for j in range(grid_size):
                point = Point(X[i, j], Y[i, j])
                velocity = self.get_velocity(point, time)
                U[i, j] = velocity.x
                V[i, j] = velocity.y

        return X, Y, U, V