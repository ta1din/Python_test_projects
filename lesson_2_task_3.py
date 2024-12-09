import math

# Функция для вычисления площади квадрата
def square(side):
    # Вычисляем площадь квадрата
    area = side * side
    # Если аргумент не целое число, округляем результат вверх
    return math.ceil(area)

# Ввод стороны квадрата
side_length = float(input("Введите сторону квадрата: "))

# Вызов функции и вывод результата
result = square(side_length)
print(f"Площадь квадрата со стороной {side_length}: {result}")