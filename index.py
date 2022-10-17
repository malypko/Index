# Index of line
word = "Malypko"
print(word[1])

# Count of line simbols
word = "Malypko"
print(len(word))

# Count coincidence simbol in the line
word = "Malypko"
print(word.count('M'))

# Upper
word = "Malypko"
print(word.upper())

# Isupper
word = "Malypko"
print(word.isupper())

# Islower
word = "alypko"
print(word.islower())

# lower
word = "Malypko"
print(word.lower())

# capitalize
word = "MALypko"
print(word.capitalize())

# find
word = "Malypko"
print(word.find('y'))

# split
word = "Malypko, Maxim, Elena"
print(word.split(", "))

# split 2
word = "Malypko, Maxim, Elena"
name = word.split(', ')
print(name[1])

# split 2 + join
word = "Malypko, maxim, elena"
name = word.split(', ')
for i in range(len(name)):
    name[i] = name[i].capitalize()
result = ", ".join(name)
print(result)

# Срезы (стартовый, конечный)
word = "Malypko"
print(word[0:4]) # от - до
print(word[4:7]) # от - до
print(word[4:-1]) # от - до конца, но заминусом последнего
print(word[1:-1:3]) #шаг переходов

lis = [6, 7, "Strong", True, 6.5]
print(lis[2]) # только второй
print(lis[2:]) # со второго до конца
print(lis[2:-1]) # со второго до конца без последнего
print(lis[2:5:2]) # со второго до пятого с шагом два
print(lis[:4:]) # выводим только до 4 элемента
print(lis[::-1]) # переворачиваем список
print(lis[::2]) # вывод через одного


