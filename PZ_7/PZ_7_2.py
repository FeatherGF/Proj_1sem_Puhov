# Дана строка, состоящая из русских слов, набранных заглавными буквами и разделенных пробелами (одним или
# несколькими). Преобразовать каждое слово в строке, заменив в нем все последующие вхождения его первой буквы на
# символ ".". Например, слово "МИНИМУМ" надо преобразовать в слово "МИНИ.У.". количество пробелов между словами не
# изменять.
word = input('Введите слово: ')
new_word = word[0] + word[1:].replace(word[0], '.')  # сохраняю первую букву строки, потом на срезе все без первой буквы
# заменяю все одинаковые с первым символом буквы на точку
print(new_word)
