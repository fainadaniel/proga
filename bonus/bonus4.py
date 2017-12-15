a = int(input("Surprize! I can translate into two codes. Press 1 if you want me to translate into русский кирпичный and 2 if you want me to translate into язык калле блюмквиста"))
if a == 1: 
    phrase = "telaviv"
    h = []
    while phrase !='':
        print((' ').join(h))
        phrase = input("give me a word\n") #saving the phrase
        words = phrase.split(" ")#splitting into words
        h = []
        for w in range (len(words)):#for every word
            l = "" #rewrite l
            m = [] #rewrite m
            for y in range (len(words[w])): #for every letter in current word
                m.append((words[w])[y]) # add it to rewritten m so m is a split of letters
                l = ("").join(m) #l is the copy of current word
            for g in range(len(m)): #for every letter in split of the currend word
                if(m[g]) == "а": #if it is the vowel
                    u = l.split("а") #so u is the first word split in two
                    l = ('аса').join(u) #so l is the first word with first vowel replaced with longer part
                    break
            for g in range(len(m)):
                if(m[g]) == "о": #if the letter is another vowel
                    u = l.split("о")
                    l = ('осо').join(u)
                    break
            for g in range(len(m)):
                if(m[g]) == "у":
                    u = l.split("у")
                    l = ('усу').join(u)
                    break
            for g in range(len(m)):
                if(m[g]) == "ы":
                    u = l.split("ы")
                    l = ('ысы').join(u)
                    break
            for g in range(len(m)):
                if(m[g]) == "и":
                    u = l.split("и")
                    l = ('иси').join(u)
                    break
            for g in range(len(m)):
                if(m[g]) == "э":
                    u = l.split("э")
                    l = ('эсэ').join(u)
                    break
            for g in range(len(m)):
                if(m[g]) == "я":
                    u = l.split("я")
                    l = ('яся').join(u)
                    break
            for g in range(len(m)):
                if(m[g]) == "ё":
                    u = l.split("ё")
                    l = ('ёсё').join(u)
                    break
            for g in range(len(m)):  
                if(m[g]) == "ю":
                    u = l.split("ю")
                    l = ('юсю').join(u)
                    break
            for g in range(len(m)):
                if(m[g]) == "е":
                    u = l.split("е")
                    l = ('есе').join(u)
                    break
            h.append(l)
if a == 2:
    
    phrase = "telaviv"
    h = []
    z = ["а", "э", "о", "у", "и", "ы", "е", "я", "ю", "ё"]

    while phrase !='':
        print((' ').join(h))
        phrase = input("give me a word\n") #saving the phrase
        words = phrase.split(" ")#splitting into words
        h = []
        for w in range (len(words)):#for every word
            l = "" #rewrite l
            m = [] #rewrite m
            for y in range (len(words[w])): #for every letter in current word
                m.append((words[w])[y]) # add it to rewritten m so m is a split of letters
                kl = []
                vo = []
                l = ("").join(m) #l is the copy of current word
            m.append(' ')
            for g in range(len(m)): #for every letter in split of the currend word
                if(m[g]) == "б": #if it is the vowel
                    u = l.split("б") #so u is the first word split in two
                    l = ('боб').join(u) #so l is the first word with first vowel replaced with longer part
                    break
            for g in range(len(m)):
                if(m[g]) == "в":
                    u = l.split("в")
                    l = ('вов').join(u)
                    break
            for g in range(len(m)):
                if(m[g]) == "г":
                    u = l.split("г")
                    l = ('гог').join(u)
                    break
            for g in range(len(m)):
                if(m[g]) == "д":
                    u = l.split("д")
                    l = ('дод').join(u)
                    break
            for g in range(len(m)):
                if(m[g]) == "ж":
                    u = l.split("ж")
                    l = ('жож').join(u)
                    break
            for g in range(len(m)):
                if(m[g]) == "з":
                    u = l.split("з")
                    l = ('зоз').join(u)
                    break
            for g in range(len(m)):
                if(m[g]) == "й":
                    u = l.split("й")
                    l = ('йой').join(u)
                    break
            for g in range(len(m)):
                if(m[g]) == "к":
                    u = l.split("к")
                    l = ('кок').join(u)
                    break
            for g in range(len(m)):  
                if(m[g]) == "л":
                    u = l.split("л")
                    l = ('лол').join(u)
                    break
            for g in range(len(m)):
                if(m[g]) == "м":
                    u = l.split("м")
                    l = ('мом').join(u)
                    break
            for g in range(len(m)):
                if(m[g]) == "н":
                    u = l.split("н")
                    l = ('нон').join(u)
                    break
            for g in range(len(m)):
                if(m[g]) == "п":
                    u = l.split("п")
                    l = ('поп').join(u)
                    break
            for g in range(len(m)):
                if(m[g]) == "р":
                    u = l.split("р")
                    l = ('рор').join(u)
                    break
            for g in range(len(m)):
                if(m[g]) == "с":
                    u = l.split("с")
                    l = ('сос').join(u)
                    break
            for g in range(len(m)):
                if(m[g]) == "т":
                    u = l.split("т")
                    l = ('тот').join(u)
                    break
            for g in range(len(m)):
                if(m[g]) == "ф":
                    u = l.split("ф")
                    l = ('фоф').join(u)
                    break
            for g in range(len(m)):
                if(m[g]) == "х":
                    u = l.split("х")
                    l = ('хох').join(u)
                    break
            for g in range(len(m)):
                if(m[g]) == "ц":
                    u = l.split("ц")
                    l = ('цоц').join(u)
                    break
            for g in range(len(m)):  
                if(m[g]) == "ч":
                    u = l.split("ч")
                    l = ('чоч').join(u)
                    break
            for g in range(len(m)):
                if(m[g]) == "ш":
                    u = l.split("ш")
                    l = ('шош').join(u)
                    break
            for g in range(len(m)):
                if(m[g]) == "щ":
                    u = l.split("щ")
                    l = ('щощ').join(u)
                    break
            for g in range(len(m)):
                if(m[g]) == "я" and g == 0:
    #                print(g, "я в нач")
                    u = l.split("я")
                    l = ('йойа').join(u)
                    break
                elif(m[g]) == "я" and (m[g-1]) in z:
    #                print(g, "я поствок")
                    for x in range(g-1, g+1, 1):
                        vo.append(m[x])
                    ty = ("").join(vo)
    #                print(ty)
                    kl = l.split(ty)
                    kl.append(' ')
                    u = [kl[0]]+[vo[0]]+['йойа']+[kl[1]]
                    l = ('').join(u)
    #                print(l, "-l")
            for g in range(len(m)):
    #            print(m[g])
                vo = []
                if(m[g]) == "е" and g == 0:
    #                print(g, "е в нач")
                    u = l.split("е")
                    l = ('йойэ').join(u)
                elif(m[g]) == "е" and (m[g-1]) in z:
    #                print(g, "е поствок")
    #                print(m)
                    for x in range(g-1, g+1, 1):
                        vo.append(m[x])
    #                print(vo)
                    ty = ("").join(vo)
    #                print(ty)
                    kl = l.split(ty)
                    kl.append(' ')
                    u = [kl[0]]+[vo[0]]+['йойэ']+[kl[1]]
                    l = ('').join(u)
    #                print(l, "-l")
            for g in range(len(m)):
                if(m[g]) == "ю" and g == 0:
    #                print(g, "ю в нач")
                    u = l.split("ю")
                    l = ('йойу').join(u)
                    break
                elif(m[g]) == "ю" and (m[g-1]) in z:
    #                print(g, "ю поствок")
                    for x in range(g-1, g+1, 1):
                        vo.append(m[x])
                    ty = ("").join(vo)
    #                print(ty)
                    kl = l.split(ty)
                    kl.append(' ')
                    u = [kl[0]]+[vo[0]]+['йойу']+[kl[1]]
                    l = ('').join(u)
    #                print(l, "-l")
            for g in range(len(m)):  
                if(m[g]) == "ё" and g == 0:
    #                print(g, "ё в нач")
                    u = l.split("ё")
                    l = ('йойо').join(u)
                    break
                elif(m[g]) == "ё" and (m[g-1]) in z:
    #                print(g, "ё поствок")
                    for x in range(g-1, g+1, 1):
                        vo.append(m[x])
                    ty = ("").join(vo)
    #                print(ty)
                    kl = l.split(ty)
                    kl.append(' ')
                    u = [kl[0]]+[vo[0]]+['йойо']+[kl[1]]
                    l = ('').join(u)
    #                print(l, "-l")
            h.append(l)
            
