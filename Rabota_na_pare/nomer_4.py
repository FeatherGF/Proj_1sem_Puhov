# Рекурсивная функция - возвращает ряд Фибоначчи в виде списка.
# Параметр n - максимальное значение в списке.
def fib(n):
    global my_list
    if n != 0:
        my_list.append(my_list[-1] + my_list[-2])
        fib(n - 1)
    return my_list


my_list = [1, 2]
print(fib(15))
