# В матрице найти сумму элементов первых двух строк.
from random import randint

rows = randint(2, 7)
columns = randint(2, 7)
matrix = [[randint(-5, 5) for j in range(columns)] for i in range(rows)]  # создание матрицы
summary = 0
print('Матрица:')
for i in range(rows):
    for j in range(columns):
        print(matrix[i][j], end='\t')
        if i < 2:
            summary += matrix[i][j]  # сложение элементов первых двух строк
        else:
            continue
    print()
print(f"Сумма первых двух строк: {summary}")
