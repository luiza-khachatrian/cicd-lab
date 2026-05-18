# Документация: Калькулятор

## Описание проекта
Простой калькулятор на Python с поддержкой базовых арифметических операций.
Проект используется как пример для настройки CI/CD с GitHub Actions.

## Установка

```bash
pip install -r requirements.txt
```

## Функции

### `add(a, b)`
Возвращает сумму двух чисел.
```python
add(2, 3)  # → 5
```

### `subtract(a, b)`
Возвращает разность a - b.
```python
subtract(10, 4)  # → 6
```

### `multiply(a, b)`
Возвращает произведение двух чисел.
```python
multiply(3, 4)  # → 12
```

### `divide(a, b)`
Возвращает результат деления a / b.
Вызывает `ValueError` при делении на ноль.
```python
divide(10, 2)  # → 5.0
```

### `power(base, exponent)`
Возводит base в степень exponent.
```python
power(2, 3)  # → 8
```

### `square_root(number)`
Возвращает квадратный корень числа.
Вызывает `ValueError` для отрицательных чисел.
```python
square_root(9)  # → 3.0
```

## Запуск тестов

```bash
pytest -v
```

## CI/CD

Проект использует GitHub Actions для автоматического тестирования при каждом коммите.
Workflow файл: `.github/workflows/main.yml`
