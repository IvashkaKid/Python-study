number_one = int(input())
number_two = int(input())

if number_one < number_two:
    print("Первое число меньше второго")
elif number_one > number_two:
    print("Первое число больше второго", end=' ')
    if number_one >= (number_two * 3):
        print("в 3 раза")
