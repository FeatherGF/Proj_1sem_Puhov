# Известны марки машин, выпускаемые в данной стране и экспортируемых в N заданных стран. Определить какие марки машин
# были доставлены во все указанные страны, какие в некоторые из стран и какие не доставлены ни в одну страну.
import random

n = int(input('Введите количество стран: '))
brands = {'Audi', 'Tesla', 'Lamborghini', 'Mercedes', 'Mitsubishi', 'Bugatti', 'Porsche'}
countries = {'Poland', 'Russia', 'England', 'USA', 'Argentina', 'Mexico', 'China', 'Japan', 'Thailand', 'Netherlands',
             'Norway'}
exports = [{random.choice([*brands]) for j in range(random.randint(1, len(brands) + 1))} for i in range(1, n + 1)]
# Создается список, элементы которого являются множествами. Эти множества создаются генератором. Из множества brands
# берется случайное количество раз случайная марка машины
dictionary = dict(zip(countries, exports))  # создаю словарь ключ - страна, значение - множество марок машин этой страны
for key, value in dictionary.items():
    print(f"Марки машин в {key}: {', '.join(list(value))}.", )
print()
for brand in brands:
    count = 0
    my_list = []
    for key, value in dictionary.items():  # проверка на наличие каждой марки в каждой стране
        if brand in dictionary[key]:
            count += 1
            my_list.append(key)
    if count == len(exports):
        print(f"{brand} экспортируется во все страны: {', '.join(my_list)}.")
    elif count > 0:
        print(f"{brand} экспортируется только в некоторые из стран: {', '.join(my_list)}.")
    else:
        print(f"{brand} не экспортируется ни в одну страну.")
