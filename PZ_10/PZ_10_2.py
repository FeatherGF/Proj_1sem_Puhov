# Из предложенного текстового файла (text18-20.txt) вывести на экран его содержимое,
# количество символов в тексте. Сформировать новый файл, в который поместить строку
# наибольшей длины.

with open('text18-20.txt', 'r+', encoding='utf-8') as inf:  # для каждого прочтения из файла приходится создавать новую
    chars = inf.read()                                      # конструкцию with open, поэтому я открываю файл 3 раза
    print(chars, end='\n\n')
    print(f'Количество символов в тексте: {len(chars)}')

with open('text18-20.txt', 'r', encoding='utf-8') as inf2:
    n = 0
    for line in inf2:
        z = len(line.strip())  # высчитывание наибольшей длины строки
        n = z if z > n else n

with open('text18-20.txt', 'r', encoding='utf-8') as inf3:
    with open('result2.txt', 'w', encoding='utf-8') as result:
        for line2 in inf3:
            x = line2.strip()
            if n == len(x):
                print(x, file=result, end='')  # вывод в файл строки наибольшей длины
