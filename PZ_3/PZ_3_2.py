# Даны два числа. Вывести вначале большее, а затем меньшее из них
a, b = input('Введите первое число: '), input('Введите второе число: ')
while type(a) != int:
    try:
        a = int(a)                  # обработка исключений
    except ValueError:
        print('Неправильно ввели первое число!')
        a = input('Попробуйте еще раз: ')
while type(b) != int:
    try:
        b = int(b)                  # обработка исключений
    except ValueError:
        print('Неправильно ввели второе число!')
        b = input('Попробуйте еще раз: ')
print(f'{a if a > b else b} большее из двух чисел')
print(f'{b if a > b else a} меньшее из двух чисел')
