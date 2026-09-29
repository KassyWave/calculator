def add(a, b):
    """Возвращает сумму двух чисел.
        Пример: add(2, 3) -> 5
    """
    return a + b

def subtract(a, b):
    """Возвращает разность двух чисел.
        Пример: subtract(5, 3) -> 2
    """
    return a - b

def multiply(a, b):
    """Возвращает произведение двух чисел.
        Пример: multiply(4, 5) -> 20
    """
    return a * b

def divide(a, b):
    """Возвращает частное двух чисел.
        Пример: divide(10, 2) -> 5.0
        Исключение: ValueError: если b == 0.
    """
    if b == 0:
        raise ValueError("Деление на ноль невозможно.")
    return a / b

def power(a, b):
    """Возвращает число a в степени b.
        Пример: power(2, 3) -> 8
    """
    return a ** b

def square_root(a: float) -> float:
    """Возвращает квадратный корень числа a.
    Пример:square_root(9) -> 3.0
    Исключение: ValueError: если a < 0.
    """
    if a < 0:
        raise ValueError("Корень из отрицательного числа не определён.")
    return a ** 0.5