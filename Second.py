string = str(input())

count = 0

for i in string:
    count += 1
    
    if count == 3:
        continue
    
    if i == "с":
        print("В строке встретился символ", i)
        
    if len(string) != count:
        print(i)

print("Длинна строки:",count)
