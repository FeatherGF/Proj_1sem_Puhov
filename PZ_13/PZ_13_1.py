# В последовательности на n целых элементов в первой ее половине найти количество положительных элементов.
from random import randint

n = int(input('Введите n целых элементов в списке: '))
my_list = [randint(-100, 100) for i in range(n)]
print('Изначальный список: ', *my_list)
new_list = [i for i in my_list[:int(len(my_list) / 2)] if i > 0]  # этот срез - половина исходного списка
print(f'Количество положительных элементов в первой половине: {len(new_list)}')
