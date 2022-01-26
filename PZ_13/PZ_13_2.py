# Из заданной строки отобразить только символы нижнего регистра. Использовать библиотеку string. Строка 'In PyCharm,
# you can specify third-party standalone applications and run them as External Tools'.
from string import ascii_lowercase
phrase = 'In PyCharm, you can specify third-party standalone applications and run them as External Tools'
print('Все символы нижнего регистра из строки: ')
print(*list(filter(lambda x: x in ascii_lowercase, phrase)))
