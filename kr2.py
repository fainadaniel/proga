def count():
    with open ('mystem.xml', encoding = 'utf-8') as f:
        mystem = f.read()
        myst = mystem.split()
        for a in range (0, len(myst), 1):
            if myst[a] == '<se>':
                b = a
            if myst[a] == '</se>':
                c = a
    return(c-b-1)
print(count())

def supercount():
    with open ('mystem.xml', encoding = 'utf-8') as f:
        mystem = f.read()
        myst = mystem.split("\n")
        futuredict = []
        dictionary = dict()
        l = 0
        for a in myst:
            if a.startswith('<w>'):
                b = a.split()
                for c in b:
                    if c.startswith('gr') and c not in futuredict:
                        futuredict.append(c)
        
        for m in range (len(futuredict)):
            for g in range (len(myst)):
                l = l+1
                if myst[g] == m:
                    dictionary.update({futuredict[m]:l})
        print(dictionary)
    return()
supercount()
