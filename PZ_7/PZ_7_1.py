# Дано положительное число. Вывести символы, изображающие цифры этого числа (в порядке слева направо)
number = input('Введите положительное число: ')
my_list = []
for i in range(0, len(number), 2):  # разбитие числа на двузначные
    my_list.append(number[i:2 + i])
print(*my_list)
for j in my_list:
    print(chr(int(j)), end=' ')
