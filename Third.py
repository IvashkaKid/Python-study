string = str(input())

max_popular = 0
popular = 0
word_popular = ""
word_max_len = ""
max_len = 0

array = string.split(" ")

for i in array:
    
    popular = 0

    if len(i) > max_len:
        max_len = len(i)
        word_max_len = i
        
    for j in array:
        if i == j:
            popular += 1
            
    if popular > max_popular:
        word_popular = i
        max_popular = popular
        
print("Наиболее встречающееся слово: ",word_popular)
print("Наиболее длинное слово: ",word_max_len)

