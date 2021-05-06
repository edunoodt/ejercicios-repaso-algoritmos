def pluralize(lista):
    word = set()
    words = set()
    for i in lista:
        if i in word:
            words.add(i+'s')
        else:
            word.add(i)

    return words

def same_length(secuencia):
    v = secuencia
    cont1 = 0
    cont0 = 0
    same = False
    i=0
    while i < len(v)-1 and not same:
        if v[i] == '0':
            cont0 += 1
        else:
            cont1 += 1
        if v[i] == v[i+1]:
            i += 1
        else:
            if cont0 == cont1:
                same = True
            else:
                if v[i+1] == '0':
                    cont0 = 0
                else:
                    cont1 = 0
                i += 1
    return same

if __name__ == '__main__':
    print(pluralize(["cow", "pig", "cow", "cow"]))
    print(same_length("110011100010"))
