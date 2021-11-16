# condition
from random import randint
n = int(input())
my_list = [randint(1, 9) for i in range(1, n + 1)]
k, L = int(input()), int(input())
sr_arif, counter = 0, 0
print(my_list)
for i in range(len(my_list))[k:L+1]:
    sr_arif += i
    counter += 1
    print(sr_arif)
sr_arif /= counter
print(sr_arif, counter)
