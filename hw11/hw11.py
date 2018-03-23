import re
m = []
o = []
with (open ("new 2.txt", encoding ="utf-8")) as f:
    for line in f:
        m.append(line)
    m.append(" love and peace")
    n = ('').join(m)
    forms = re.findall('съе[слшвдм][ешьиатия\s]...\S.', n)    
    for x in forms:
        l = x.split(' ')
        k = l[0]
        if not k in o:
            o.append(k)
    print (o)
