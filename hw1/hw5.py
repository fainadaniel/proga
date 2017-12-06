a = "go"
f = open("hwlastest.txt", "w")
while a != "" :
    a = input("give me a word\n")
    n = 0
    m = 1
    if len(a)%3:
        k=len(a)
        for x in range ((k)//3):
            f.write(a[n])
            n = n+3
            f.write(a[m])
            m = m+3
    elif (len(a)+1)%3:
        k=len(a)+1
        for x in range ((k)//3):
             f.write(a[n])
             n = n+3
             f.write(a[m])
             m = m+3
    else:
        k=len(a)+1
        for x in range ((k)//3):
             f.write(a[n])
             n = n+3
             f.write(a[m])
             m = m+3
f.close()
