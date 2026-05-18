# Тесты для калькулятора
# pytest сам найдёт этот файл и запустит все функции начинающиеся с test_

import pytest
from calculator import add, subtract, multiply, divide

#Тесты для сложения
def test_add_positive_numbers():
    """Проверяем что 2 + 3 = 5"""
    assert add(2, 3) == 5

def test_add_negative_numbers():
    """Проверяем сложение с отрицательными числами"""
    assert add(-1, -1) == -2

def test_add_zero():
    """Любое число + 0 = само число"""
    assert add(5, 0) == 5

# Тесты для вычитания
def test_subtract():
    """Проверяем что 10 - 4 = 6"""
    assert subtract(10, 4) == 6

def test_subtract_negative():
    """Вычитание отрицательного = прибавление"""
    assert subtract(5, -3) == 8

#Тесты для умножения
def test_multiply():
    """3 * 4 = 12"""
    assert multiply(3, 4) == 12

def test_multiply_by_zero():
    """Любое число * 0 = 0"""
    assert multiply(100, 0) == 0

#Тесты для деления
def test_divide():
    """10 / 2 = 5.0"""
    assert divide(10, 2) == 5.0

def test_divide_by_zero():
    """
    Проверяем что при делении на 0 выбрасывается ValueError.
    pytest.raises перехватывает ошибку — если ошибка есть, тест ПРОШЁЛ.
    """
    with pytest.raises(ValueError):
        divide(5, 0)


# Тесты для новых функций (ветка development)

def test_power():
    """2 в степени 3 = 8"""
    assert power(2, 3) == 8

def test_power_zero():
    """Любое число в степени 0 = 1"""
    assert power(5, 0) == 1

def test_square_root():
    """Корень из 9 = 3.0"""
    assert square_root(9) == 3.0

def test_square_root_negative():
    """Корень из отрицательного числа должен вызвать ValueError"""
    with pytest.raises(ValueError):
        square_root(-1)
