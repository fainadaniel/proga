a = input("give me a word or a phrase\n")
b = a.split()
g = [] #b - это сплит со всей фразой
for x in range(len(b)):
    c = b[x] # c - это стринг с одним словом
    d = []
    for y in range (len(c)):       
        d.append(c[y]) # d - это сплит с одним словом по буквам
    if c[0] == 'a' or c[0] == 'u' or c[0] == 'o' or c[0] == 'i' or c[0] == 'e' or c[0] == 'y':
        d.append('way ')
    else:
        for z in range(len(c)):
            if d[0] != 'a' and d[0] != 'u' and d[0] != 'o' and d[0] != 'i' and d[0] != 'e' and d[0] != 'y':
                e = d[0]
                d.remove(d[0])
                d.append(e)
            if d[0] == 'a' or d[0] == 'u' or d[0] == 'o' or d[0] == 'i' or d[0] == 'e' or d[0] == 'y':
                break
        d.append('ay ')
    f = ''.join(d)
    g.append(f)
print(''.join(g))

