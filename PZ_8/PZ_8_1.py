# Используя словарь посчитать количество уникальных слов в заданном предложении «Изучаем язык Питон». Вывести на
# экран каждую пару «ключ:значение».
line = 'Изучаем язык Питон'
# line = 'Изучаем язык Питон Java Питон язык Ruby Питон Питон язык'  # для проверки на уникальность
lst = line.split()
counter = []
for i in lst:
    counter.append(line.count(i))  # заношу в список сколько раз повторяется каждое слово в строке
dictionary = dict(zip(lst, counter))  # создаю словарь в котором ключ - слово, значение - количество его повторений
print(f'Изначальная строка: {line}')
print('Пары в словаре:')
for key in dictionary.keys():
    print(f'\t{key}: {dictionary[key]}')
count = 0
for value in dictionary.values():
    if value == 1:
        count += 1
print(f'Количество уникальных слов: {count}')