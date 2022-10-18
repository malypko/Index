#tuple
data = (4, 6, 7, 3, 5, 6, True, 5.6, 'Hello')
print(data[1:5])

#count колво совподений
print(data.count(6))

#Длина кортежа
print(len(data))

print(data)

for i in data:
    print(i)
# преобразование списка в кортеж
nums = [5, 7, 9]
new_data = tuple(nums)
word = tuple('Hello word')
print(word)
print(new_data)