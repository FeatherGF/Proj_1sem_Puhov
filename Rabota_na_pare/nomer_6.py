# Возведение числа x в степень y
def my_pow(x, y):
    return 1 if y == 0 else x * pow(x, y-1)


print(my_pow(2, 4))
