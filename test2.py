"""
Добро пожаловать в самую лучшую программу для вычисления квадратного корня
из заданного числа.
"""
from math import sqrt


def calculate_square_root(number: float) -> float:
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number: float) -> None:
    """Проверка положительного значения для переменной."""
    if your_number <= 0:
        return
    return print(calculate_square_root(your_number))


print(f" Мы вычислили квадратный корень из введённого вами числа. "
      f"Это будет: {calc(25.5)}")
