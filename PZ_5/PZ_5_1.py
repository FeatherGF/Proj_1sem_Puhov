# составить функцию, которая напечатает сорок любых символов
def chars(a):
    i = 0
    while i <= 40:
        print(a, end='')
        i += 1


stroka = input('Введите 1 символ: ')
while type(stroka) != str or len(stroka) != 1:
    stroka = input('Вы ввели не один символ!\nПопробуйте еще раз: ')
chars(stroka)

# сделал через библиотеку
# from random import choice
# string = "qwertyuioplkjhgfdsazxcvbnm"
# def random_40_chars():
#     for i in range(40):
#         char = choice(string)
#         print(char, end='')
# random_40_chars()
