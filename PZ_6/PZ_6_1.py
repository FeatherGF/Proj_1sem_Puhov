# Дан список размера N и целые числа K и L (1 < K < L < N). Найти среднее арифметическое элементов списка с номерами
# от K до L включительно
from random import randint

n = int(input('Введите длину списка: '))
my_list = [randint(1, 100) for i in range(n)]  # создание списка с случайными элементами
k, L = int(input('Введите К: ')), int(input('Введите L: '))
print(
    f'Исходный список: {my_list}\n'
    f'На срезе: {my_list[k - 1:L]} Среднее арифметическое: {sum(my_list[k - 1:L]) / len(my_list[k - 1:L])}')
# вычисление суммы элементов списка на срезе от K до L включительно. Затем деление на длину списка с таким же срезом.
