# calculator.py
# Простой калькулятор - основной код нашего проекта

def add(a, b):
    """Сложение двух чисел"""
    return a + b

def subtract(a, b):
    """Вычитание: a минус b"""
    return a - b

def multiply(a, b):
    """Умножение двух чисел"""
    return a * b

def divide(a, b):
    """
    Деление a на b.
    Если b = 0, выбрасываем ошибку — делить на ноль нельзя.
    """
    if b == 0:
        raise ValueError("Деление на ноль невозможно!")
    return a / b
