while True:
    string = str(input("Введите строку: "))

    count = 0
    letter = "с"
    waring = 0
    length = len(string)

    for i in string:
        count += 1
    
        if count == 3:
                print(count,")","Третий символ пропущен")
                continue
    
        if i == letter:
            waring += 1
        
        if length != count:
            print(count,")",i)
        else:
            print(count,")","")
        
    if waring != 0:
        print("В строке встретился символ: ", letter)

    print("Длинна строки:",count,"\n")
