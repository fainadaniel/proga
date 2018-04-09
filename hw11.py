import re
with open('dinosaur.txt', encoding = 'utf-8') as f:
    text = f.read()
    text1 = re.sub('динозавр','кот', text)
    text2 = re.sub('Динозавр','Кот', text1)
    print(text2)
print("MEEEEOUW")
