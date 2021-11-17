# составить функцию, которая напечатает сорок любых символов
def chars(a):
    i = 0
    while i < 40:
        print(a, end='')    # функция, который выводит 40 раз введенный символ
        i += 1


stroka = ''
while not stroka.isalpha() or len(stroka) != 1:     # обработка исключений
    try:
        stroka = input('Введите 1 букву: ')
        if len(stroka) != 1:
            print('Вы ввели не один символ!')
            raise ValueError
    except ValueError:
        stroka = input('Введите 1 букву: ')
        if len(stroka) != 1:
            print('Вы ввели не одну букву!')
chars(stroka)
