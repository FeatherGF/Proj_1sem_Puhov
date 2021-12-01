# Дано положительное число. Вывести символы, изображающие цифры этого числа (в порядке слева направо)
number = input('Введите положительное число: ')
my_list = []
for i in number:
    my_list.append(chr(int(i)))
print(my_list)
