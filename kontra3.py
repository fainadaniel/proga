with open("ozhegov.txt", encoding = "utf-8") as f:
    m = 0
    n = "chuchu"
    o = []
    q = []
    while(n != ""):
        n = input("give me a word\n")
        o.append(n)
#        q = o
    for line in f:
            for x in range(len(o)-1):
                if line.startswith(o[x]):
                    l = str(x)
#                    q.append(l)
                    linia = line.strip()
                    words = linia.split("|")
                    print(words[0], '-', words[3], '-', words[1])
        
#print (q)
