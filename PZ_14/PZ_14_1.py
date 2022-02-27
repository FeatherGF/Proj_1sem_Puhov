# Из текстового файла (writer.txt) выбрать фамилии писателей, посчитать количество
# фамилий. Создать новый файл, в котором выполнить замену слова «роман» на слово «произведение»
import re

with open('writer.txt', 'r', encoding='utf-8') as inf:
    text = inf.read()
reg = re.compile(r'^(\w+\S\w+)\s\w[.,\s]\w[.,\s]', re.M)
authors = re.findall(reg, text)
print(f'Количество фамилий: {len(authors)}')
new_text = text.replace('роман ', 'произведение ')
new_text = new_text.replace('романов', 'произведений')  # замена слов
new_text = new_text.replace('романа', 'произведения')
with open('result.txt', 'w', encoding='utf-8') as res:
    print(new_text, file=res)
