# В матрице найти минимальный и максимальные элементы.
from random import randint

rows = randint(2, 6)
columns = randint(2, 6)
matrix = [[randint(-20, 20) for j in range(columns)] for i in range(rows)]  # создание матрицы

maximum = max(matrix[0])  # нахождение максимального и минимального элемента в первой строке матрицы
minimum = min(matrix[0])
print('Матрица:')

for i in range(rows):
    maximum = max(matrix[i]) if max(matrix[i]) > maximum else maximum  # сравнение максимального элемента из первой
    # строки с максимальным из следующей строки и записи наибольшего в переменную maximum
    minimum = min(matrix[i]) if min(matrix[i]) < minimum else minimum  # аналогично только находится минимальное
    for j in range(columns):
        print(matrix[i][j], end='\t')
    print()

print(f'Минимальный элемент: {minimum}\n'
      f'Максимальный элемент: {maximum}')
