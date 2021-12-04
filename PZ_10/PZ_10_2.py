# Из предложенного текстового файла (text18-20.txt) вывести на экран его содержимое,
# количество символов в тексте. Сформировать новый файл, в который поместить строку
# наибольшей длины.
with open('text18-20.txt', 'r', encoding='utf-8') as inf:
    chars = inf.read().strip()
    print(chars)
    chars_list = list(chars)
    print(chars_list)
    # chars_list.pop()
    print(f'Количество символов = {len(chars)}')
