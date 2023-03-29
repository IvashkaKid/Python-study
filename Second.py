while True:
    string = str(input("Введите строку: "))

    count = 0
    letter = "с"
    waring = 0

    for i in string:
        count += 1
    
        if count == 3:
            print("Третий символ пропущен")
            continue
    
        if i == letter:
            waring += 1
        
        if len(string) != count:
            print(i)
        else:
            print("Последний символ не выведен\n")
        
    if waring != 0:
        print("В строке встретился символ: ", letter)

    print("Длинна строки:",count,"\n")
