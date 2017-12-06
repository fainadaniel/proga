a = 1
f = []
k = 0
while a != "":
    a = input("give me a number\n")
    f.append(a)
print (f)
for x in range (0, len(f)-1, 1):
    k = k + int(f[x])
print("average:")
print(k//(len(f)-1))

m = int(f[1])
for x in range (0, len(f)-1, 1):
    if int(f[x]) < m:
        m = int(f[x])
print("minimum:")
print(m)

n = int(f[1])

for x in range (0, len(f)-1, 1):
     if int(f[x]) > n:
        n = int(f[x])
        
print("maximum:")
print(n)

s = input('Ja tak poniala etu zadachu, chto nuzhno vydatj srednee arifmeticheskoe vseh vvedennyh chisel, ne vkluchaja poslednee pustoe. Esli nushno bylo vkluchatj pustoe, napishite yes. Esli i tak norm, napishite 'no' \n')
if s == 'yes':
    for x in range (0, len(f)-1, 1):
        k = k + int(f[x])
    print("sorry, true average:")
    print(k//(len(f)))
