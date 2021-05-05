lista = ['cow', 'pig', 'cow']
word = set()
words = set()
for i in lista:
    if i in word:
        words.add(i+'s')
    else:
        word.add(i)
print(words)
