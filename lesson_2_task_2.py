# Функция, определяющая, является ли год високосным
def is_year_leap(year):
    return year % 4 == 0

# Выберите год и вызовите функцию
year = int(input("Введите год: "))
result = is_year_leap(year)

# Вывод результата
print(f"Год {year}: {result}")