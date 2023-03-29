while True:
    number_one = float(input("Введите первое число: "))
    number_two = float(input("Введите второе число: "))

    if number_one < number_two:
        print("Первое число меньше второго\n")
    elif number_one > number_two:
        print("Первое число больше второго", end=' ')
        if number_one >= (number_two * 3):
            print("в более чем 3 раза\n")
        else:
            print("\n")
