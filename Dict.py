# Словари
#counrty = {(5, 6): 3}
#print(counrty[(5, 6)])

#counrty = {'code': 'RU', 'name': 'Russian', 'population': 144}
#print(counrty['name'])

#counrty = dict(code='RU', name='Russia')
#print(counrty['name'])

counrty = {'code': 'RU', 'name': 'Russian', 'population': 144}

print(counrty.items())

for key, value in counrty.items():
    print(key, " - ", value)

print(counrty['code'])
print(counrty.get('name'))

#counrty.clear()
#print(counrty)

#Удаляем елемент с ключом Наме
#counrty.pop('name')
#print(counrty)

# Удаляем последний элемент
#counrty.popitem()
#print(counrty)

counrty['code'] = 'None'
print(counrty)


