# Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
#   Исходные данные:
#   Количество элементов:
#   Минимальный элемент:
#   Числа кратные трем:
#   Количество чисел кратных трем:
from random import randint

with open('sequence.txt', 'w', encoding='utf-8') as seq:
    for i in range(25):
        k = randint(-100, 100)
        while k == 0:
            k = randint(-100, 100)
        print(k, end=' ', file=seq)  # записывание в файл последовательности

with open('sequence.txt', 'r') as inf:
    line = [int(i) for i in inf.readline().split()]  # заношу в список последовательность из файла
    nok3 = [i for i in line if i % 3 == 0]  # создаю список элементов кратных трем
    with open('result.txt', 'w', encoding='utf-8') as res:
        print('Исходные данные:', *line, file=res)
        print(f'Количество элементов: {len(line)}', file=res)
        print(f'Минимальный элемент: {min(line)}', file=res)
        print('Числа кратные трем: ', *nok3, file=res)
        print(f'Количество чисел кратное трем: {len(nok3)}', file=res)
