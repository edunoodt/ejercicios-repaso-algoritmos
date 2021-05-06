v1 = ('000111000000111000111000111')
v = v1
cont1 = 0
cont0 = 0
same = False
cambio=True
i=0
while i < len(v)-1 and not same:
    if v[i] == '0':
        cont0 += 1
    else:
        cont1 += 1
    if v[i] == v[i+1]:
        i += 1
    else:
        print(cont0,cont1)
        if cont0 == cont1:
            same = True
            print ('pasó')
        else:
            if v[i+1] == '0':
                cont0 = 0
            else:
                cont1 = 0
            i += 1
print (same)