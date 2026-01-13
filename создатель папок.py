import os


def create_project_structure():
    """Создает структуру проекта для курсовой работы"""

    print("Создание структуры проекта...")

    # 1. Создаем папки
    folders = [
        'entities',
        'solvers',
        'fields',
        'visualization',
        'tests'
    ]

    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"✓ Создана папка: {folder}/")

    # 2. Создаем файлы с простым содержимым
    files_to_create = [
        ('entities/__init__.py', ''),
        ('entities/point.py', '# Point class will be here'),
        ('entities/trajectory.py', '# Trajectory class will be here'),
        ('entities/body.py', '# MaterialBody class will be here'),

        ('solvers/__init__.py', ''),
        ('solvers/runge_kutta.py', '# RungeKutta solver will be here'),

        ('fields/__init__.py', ''),
        ('fields/velocity_field.py', '# VelocityField class will be here'),

        ('visualization/__init__.py', ''),
        ('visualization/plotter.py', '# Plotter class will be here'),

        ('tests/__init__.py', ''),
        ('tests/test_basic.py', '# Tests will be here'),

        ('main.py', '#!/usr/bin/env python3\nprint("Проект по теории упругости")\n'),

        ('requirements.txt', 'numpy>=1.21.0\nmatplotlib>=3.5.0'),

        ('README.md', '# Elasticity Theory Project\n\nCourse work project.'),

        ('.gitignore', '__pycache__/\n*.pyc\n*.pyo\n.env\nvenv/\n*.png\n*.pdf\n')
    ]

    # 3. Создаем файлы
    for filepath, content in files_to_create:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✓ Создан файл: {filepath}")

    print("\n" + "=" * 50)
    print("СТРУКТУРА ПРОЕКТА СОЗДАНА УСПЕШНО!")
    print("=" * 50)


    return True


if __name__ == "__main__":
    try:
        create_project_structure()
    except Exception as e:
        print(f"Ошибка: {e}")