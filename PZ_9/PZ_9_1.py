# Известны марки машин, выпускаемые в данной стране и экспортируемых в N заданных стран. Определить какие марки машин
# были доставлены во все указанные страны, какие в некоторые из стран и какие не доставлены ни в одну страну.
import random

n = int(input('Введите количество стран: '))
brands = {'Audi', 'Tesla', 'Lamborghini', 'Mercedes', 'Mitsubishi', 'Bugatti', 'Porsche'}
countries = [{random.choice([*brands]) for j in range(random.randint(1, len(brands) + 1))} for i in range(1, n + 1)]
# Создается список, элементы которого являются множествами. Эти множества создаются генератором. Из множества brands
# берется случайное количество раз случайная марка машины
print('Экспортированные марки машин в разные страны:', *countries, sep='\n', end='\n' * 2)
for brand in brands:
    count = 0
    for country in countries:  # проверка каждой марки на наличие в каждом множестве
        if brand in country:
            count += 1
    if count == len(countries):
        print(f'{brand} экспортируется во все страны')
    elif count > 0:
        print(f'{brand} экспортируется только в некоторые из стран')
    else:
        print(f'{brand} не экспортируется ни в одну страну')
