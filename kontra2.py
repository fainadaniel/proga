with open("ozhegov.txt", encoding = "utf-8") as f:
    m = 0
    for line in f:
        linia = line.strip()
        words = linia.split('|')
        if words[2] != '':
            m = m+1
print(m.join("-"))
