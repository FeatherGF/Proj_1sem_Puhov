# Дано целое число N (> 0). Найти сумму 1 ** 1 + 2 ** 2 + ... N ** N.
n = input('Введите целое число: ')
while type(n) != int:
    try:
        n = int(n)
        if not n > 0:
            print('Число отрицательное!')
            n = input('Попробуйте еще раз: ')
    except ValueError:
        print('Неправильно ввели целое число!')
        n = input('Попробуйте еще раз: ')
a = 0
for i in range(1, n + 1):
    a += i ** i
print(f'Сумма 1 ** 1+ 2 ** 2 + ... + N ** N равно: {a}')
