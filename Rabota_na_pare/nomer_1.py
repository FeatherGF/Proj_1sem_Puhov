# Вычислить сумму элементов набора чисел
my_list = [i for i in range(15)]
print(my_list)


def sum_arr(arr, size):
    if size == 0:
        return 0
    else:
        return arr[size - 1] + sum_arr(arr, size - 1)


print(sum_arr(my_list, len(my_list)))
print(sum(my_list))
