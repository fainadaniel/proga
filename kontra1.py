with open("ozhegov.txt", encoding = "utf-8") as f:
    for line in f:
        linia = line.strip()
        words = linia.split("|")
        if len(words[0]) > 19:
            print(words[0])        
