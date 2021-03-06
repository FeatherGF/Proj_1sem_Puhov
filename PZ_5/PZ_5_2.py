# Дан прямоугольник, длины сторон которого равны натуральным числам А и В. Составить функцию, которая будет находить
# на сколько квадратов можно разрезать данный прямоугольник, если от него отрезать каждый раз квадрат наибольшей
# площади
def rectangle(a, b):
    area = a * b
    a = b if a > b else a       # нахождение наибольшей стороны квадрата
    square_area = a * a
    i = 0
    while area // square_area > 0:
        area -= square_area     # находим сколько раз можно отрезать квадрат, путем вычитания площади квадрата из
        i += 1                  # площади прямоугольника
    return i


width = int(input('Введите ширину прямоугольника: '))
height = int(input('Введите высоту прямоугольника: '))
print(f'От прямоугольника можно отрезать квадрат {rectangle(width, height)} раз(а)')
