from typing import Callable, List, Tuple
import numpy as np
from dataclasses import dataclass


@dataclass
class ButcherTableau:
    """Таблица Бутчера для методов Рунге-Кутты"""
    A: np.ndarray  # Матрица коэффициентов
    b: np.ndarray  # Вектор весов
    c: np.ndarray  # Вектор узлов

    @staticmethod
    def create_21() -> 'ButcherTableau':
        """Создает таблицу Бутчера 2.1 (метод средней точки)"""
        A = np.array([[0, 0],
                      [0.5, 0.5]])
        b = np.array([0, 1])
        c = np.array([0, 0.5])
        return ButcherTableau(A, b, c)


class RungeKuttaSolver:
    """Решатель ОДУ методом Рунге-Кутты"""

    def __init__(self, tableau: ButcherTableau):
        self.tableau = tableau
        self.stages = len(tableau.b)

    def solve(self, func: Callable, y0: np.ndarray, t_span: Tuple[float, float],
              dt: float = 0.01) -> Tuple[np.ndarray, np.ndarray]:
        """Решает ОДУ dy/dt = func(t, y)"""
        t_start, t_end = t_span
        num_steps = int((t_end - t_start) / dt) + 1
        times = np.linspace(t_start, t_end, num_steps)

        y = np.zeros((num_steps, len(y0)))
        y[0] = y0

        for i in range(num_steps - 1):
            t = times[i]
            k = np.zeros((self.stages, len(y0)))

            # Вычисляем стадии
            for s in range(self.stages):
                sum_Ak = np.zeros_like(y0)
                for j in range(s):
                    sum_Ak += self.tableau.A[s, j] * k[j]

                k[s] = func(t + self.tableau.c[s] * dt, y[i] + dt * sum_Ak)

            # Вычисляем следующее значение
            y[i + 1] = y[i] + dt * np.sum(self.tableau.b.reshape(-1, 1) * k, axis=0)

        return times, y