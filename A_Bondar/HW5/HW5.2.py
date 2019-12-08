# Дан текст (строк может быть много, разделенных \n). Выведите слово, которое
# в этом тексте встречается чаще всего. Если таких слов несколько, выведите
# то, которое меньше в лексикографическом порядке.

text = input('Введите текст ')
words = {}
result = []
text = ''.join(sign for sign in text if sign not in (',', '.', '?', '!', ':', ';', '(', ')',
                                                     '[', ']','{', '}', '+', '-', '/', '|',
                                                     '>', '<', '=', '#',
                                                     '$', '%', '^', '&', '*'))
text = text.lower().split()
for word in range(len(text)):
    words[text[word]] = words.get(text[word], 0) + 1
for key in words:
    if words[key] == max(words.values()):
        result.append(key)
print(sorted(result)[0])
