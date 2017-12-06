a = "go"
f = open("hwlastest.txt", "w")
while a != "" :
    a = input("give me a word\n")
    n = 0
    m = 1
    f.write("\n")
    k = len(a)
    if k % 3 == 0:
        for x in range ((k)//3):
            f.write(a[n])
            n = n+3
            f.write(a[m])
            m = m+3
    elif (k+1)% 3 == 0:
        g = (k+1)//3
        for x in range (g):
            f.write(a[n])
            n = n+3
            f.write(a[m])
            m = m+3
    else:
        h=(k+2)//3
        for x in range (h-1):
            f.write(a[n])
            n = n+3
            f.write(a[m])
            m = m+3
        f.write(a[n])
           
f.close()

f = open("hwlastest.txt", "r")
spisokslov = f.readlines()
f.close()
f = open("hwlastest.txt", "w")
#f.close()
for x in range (len(spisokslov)):
    slovo =(spisokslov[x])
    for z in range (len(slovo)-1, -1, -1):
        f.write(slovo[z])
    f.write("\n")
f.close()
f = open("hwlastest.txt", "r")
spisokovosl = f.readlines()
for x in range (len(spisokovosl)):
    print(spisokovosl[x])     
f.close()
