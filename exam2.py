import collections
with open("itartass1.html", encoding = 'utf-8') as f:
    text = f.read()
drink = text.split('lex="')
gin = []
for x in drink:
    if x[0].isupper() and x[0] != 'X':
        gin.append(x.split('"')[0])

counter = collections.Counter(gin)
print(counter)

with open ('rum.xml', 'w', encoding = 'utf-8') as u:
    for k,v in counter.items():
        u.write(k)
        u.write('\t')
        u.write(str(v))
        u.write('\t')
