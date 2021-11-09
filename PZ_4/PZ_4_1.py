# Дано вещественное число Х и целое число N (> 0). Найти значение выражения 1 - Х ** 2/(2!) + Х ** 4/(4!) + ... +
# (-1) ** N * X ** (2 * N)/((2 * N)!) (N! = 12 ... N) полученное число является приближенным значением функции
# cos в точке X.
x = input('Введите вещественное число: ')
n = input('Введите целое число: ')

while type(x) != float:         # обработка исключений
    try:
        x = float(x)
    except ValueError:
        print('Неправильно ввели вещественное число!')
        x = input('Попробуйте еще раз: ')

while type(n) != int:
    try:
        n = int(n)
        if not n > 0:
            print('Число отрицательное!')
            n = input('Попробуйте еще раз: ')
    except ValueError:
        print('Неправильно ввели целое число!')
        n = input('Попробуйте еще раз: ')

b = 0
fact = 1
for j in range(n + 1):          # проводим вычисления
    for i in range(1, (2 * j) + 1):
        fact *= i
    b += ((-1) ** j) * (x ** (2 * j)) / fact
    fact = 1
print(f'косинус числа {x}  равен {b} с точностью {n} знаков.')
