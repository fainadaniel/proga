import random
def vse ():
    def noun():
        nouns = ['Лужин ', 'Он ', 'Её отец ']
        return random.choice(nouns)

    def verb():
        verbs = ['увидел, ', 'заметил, ', 'ощутил, ', 'добавил, ', 'понял, ', 'подумал, ', 'вспомнил, ', 'вздохнул, ', 'закрыл ', 'оглянулся, ', 'положил ']
        return random.choice(verbs)
    c = verb()
    def firstpart ():
        conjs = ['как ', 'что ']
        conjs2 = ['и ', 'а ']
        what = ['дверь, ', 'коробку, ', 'книгу, ']
        if c in ['увидел, ', 'заметил, ', 'ощутил, ', 'добавил, ', 'понял, ', 'подумал, ', 'вспомнил, ']:
                return c + random.choice(conjs)
        if c in ['вздохнул, ', 'закрыл ', 'оглянулся, ', 'положил ']:
            if c in ['закрыл ', 'положил ']:
                return c + random.choice(what) + random.choice(conjs2)
            else:
                return c + random.choice(conjs2)  

    def secnoun():
        secnouns = ['эти ноги ', 'Валентинов ', 'Митька ', 'он ', 'тиканье ', 'комбинация ', 'ночь ', 'она ']
        return random.choice(secnouns)
    a = secnoun()

    def secverb():
        secverbs = ['принадлежал', 'происходил', 'подарил', 'сходил', 'влезал', 'застыл']
        return random.choice(secverbs)

    b = secverb()

    def secpart():
        if a in ['эти ноги '] :
            if b in ['сходил']:
                return a + b + 'и' + ' с ума'
            else:
                return a + b + 'и'
        if a in ['Валентинов ', 'Митька ', 'он '] :
            if b in ['сходил']:
                return a + b + ' с ума'
            else:
                return a + b
        if a in ['тиканье '] :
            if b in ['сходил']:
                return a + b + 'о' + ''
            else:
                return a + b + 'о'
        if a in ['комбинация ', 'ночь ', 'она '] :
            if b in ['сходил']:
                return a + b + 'а' + ' с ума'
            else:
                return a + b + 'а'
        

    def ending():
        endings1 = [' при его победе.', ' навсегда.', ' в парижском клубе.']
        endings2 = [' в недавний сон', ' на лавочку']
        endings3 = [' её', ' эту доску']
        endings4 = [' его невесте', ' не ему']
        if b in ['происходил', 'сходил', 'застыл']:
            return random.choice(endings1)
        if b in ['влезал']:
            return random.choice(endings2)
        if b in ['подарил']:
            return random.choice(endings3) + random.choice(endings4) + random.choice(endings1)
        if b in ['принадлежал']:
            return random.choice(endings4)


    def sentence():
        phrase =  noun() +  firstpart() + secpart() + ending()
        return phrase
    
    return sentence()



a = random.randint(5, 15)
for x in range (a):
    p = vse()
    print(p)
    

print("\n", 'Можно извиниться?')
gh = input()
if gh == "да" or gh == "Да" or gh == "yes" or gh == "Yes" or gh =="lf" or gh == "Lf":
    print("Эмм, короче я  так намудрила со сложными ни с чем не сочетающимися предложениями, что не смогла сделать, чтобы все работало если мелкие функции просто отдельно. Пришлось все пихнуть в одну. Простите. Еще простите, что функции так дебильно называются. У меня нет сил, я умираю, я иду делать АП. Мне понравилась эта игрушка.")
else:
    print("лан")
