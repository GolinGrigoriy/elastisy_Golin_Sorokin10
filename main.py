import numpy as np

from entities import Point
from entities.body import MaterialBody
from solvers.runge_kutta import RungeKuttaSolver, ButcherTableau
from fields.velocity_field import VelocityField
from Visualisation.plotter import Plotter


def main():
    """Основная функция программы"""

    # 1. Параметры из условия
    A_func = lambda t: np.exp(t)  # A(t) = e^t
    B_func = lambda t: t ** 3  # B(t) = t^3
    radius = 4.0  # Радиус окружности

    # 2. Создание объектов
    print("Создание материального тела (1/4 окружности)...")
    body = MaterialBody.create_circle_quarter(radius, num_points=30)

    print("Создание поля скоростей...")
    velocity_field = VelocityField(A_func, B_func)

    print("Создание решателя Рунге-Кутты...")
    tableau = ButcherTableau.create_21()  # Таблица Бутчера 2.1
    solver = RungeKuttaSolver(tableau)

    # 3. Параметры интегрирования
    t_start = 0.0
    t_end = 1.0
    dt = 0.01

    print(f"\nИнтегрирование траекторий от t={t_start} до t={t_end}...")

    # 4. Интегрирование траекторий для каждой точки
    new_points = []
    for i, point in enumerate(body.initial_points):
        y0 = point.as_array()
        times, solution = solver.solve(
            velocity_field.get_velocity_func(),
            y0,
            (t_start, t_end),
            dt
        )

        # Последняя точка - конечное положение
        final_point = Point.from_array(solution[-1])
        new_points.append(final_point)

        # Обновляем траекторию промежуточными точками
        for j in range(1, len(times)):
            intermediate_point = Point.from_array(solution[j])
            body.trajectories[i].points.append(intermediate_point)
            body.trajectories[i].times.append(times[j])

    # 5. Обновление тела с конечными точками
    body.update_points(new_points, t_end)

    # 6. Визуализация результатов
    print("\nПостроение графиков...")

    # Траектории
    Plotter.plot_trajectories(body, save_path='trajectories.png')

    # Формы тела
    Plotter.plot_body_shapes(body, save_path='body_shapes.png')

    # Поля скоростей и линии тока в разные моменты времени
    times_to_plot = [0.0, 0.3, 0.6, 1.0]
    x_range = (-5, 5)
    y_range = (-5, 5)

    Plotter.plot_velocity_fields(
        velocity_field,
        times_to_plot,
        x_range,
        y_range,
        save_path='velocity_fields.png'
    )

    print("\nГотово! Результаты сохранены в файлы PNG.")

    # 7. Вывод информации
    print(f"\nПараметры моделирования:")
    print(f"  - Радиус окружности: {radius}")
    print(f"  - A(t) = exp(t), B(t) = t^3")
    print(f"  - Время: от {t_start} до {t_end}")
    print(f"  - Число точек тела: {len(body.initial_points)}")
    print(f"  - Метод: Рунге-Кутта с таблицей Бутчера 2.1")


if __name__ == "__main__":
    main()