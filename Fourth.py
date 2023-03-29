import math
import random

print("Доступные операции:")
print("+ - сложение")
print("- - вычитание")
print("* - умножение")
print("/ - деление")
print("** - возведение в степень")
print("mod - модуль числа")
print("rand - случайное число")
print("! - факториал числа")
print("arccos - арккосинус числа")

while True:
    operation = input("Введите операцию: ")

    if operation == '+':
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        result = a + b
        print("Результат: ", result)

    elif operation == '-':
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        result = a - b
        print("Результат: ", result)

    elif operation == '*':
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        result = a * b
        print("Результат: ", result)

    elif operation == '/':
        a = float(input("Введите делимое: "))
        b = float(input("Введите делитель: "))
        result = a / b
        print("Результат: ", result)

    elif operation == '**':
        a = float(input("Введите число: "))
        b = float(input("Введите степень: "))
        result = a ** b
        print("Результат: ", result)

    elif operation == 'mod':
        a = float(input("Введите число: "))
        result = abs(a)
        print("Результат: ", result)

    elif operation == 'rand':
        a = float(input("Введите минимальное значение: "))
        b = float(input("Введите максимальное значение: "))
        result = random.uniform(a, b)
        print("Результат: ", result)

    elif operation == '!':
        a = int(input("Введите число: "))
        result = math.factorial(a)
        print("Результат: ", result)

    elif operation == 'arccos':
        a = float(input("Введите число: "))
        result = math.acos(a)
        print("Результат: ", result)

    else:
        print("Ошибка: неправильная операция, попробуйте ещё раз")
