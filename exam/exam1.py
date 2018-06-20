import re
with open("itartass1.html", encoding = 'utf-8') as f:
    text = f.read()
    
def title():
    tit = re.split('<title>|</title>', text)
    return tit[1]

make = text.split('\n')
cake = []
for x in make:
    if x.startswith('<w>'): 
        cake.append(x)
        
love = []
lemon = []
for y in cake:
    sweet = re.split('ana>|</w', y)
    vanilla = (sweet[len(sweet)-2]).split('`')
    nutmeg = ('').join(vanilla)
    lemon.append(nutmeg)

ginger = ' '.join(lemon)

with open('write.txt', 'w', encoding = 'cp1251') as k:
    k.write(title())
    k.write(' ')
    k.write(ginger)
