cons = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
e = "telaviv"
l = "jerusalem"
while e != '':
    m = []
    n = []
    o = []
    e = input('give me a word\n')
    t = e.split(' ') #list of words
 #   print(t, "pishu t")
    for y in t:
        a = y #a is a word
 #       print(len(a))
#        print(y)
        for x in range(len(a)):
            m.append(a[x])
 #       print (m, 'pishu m')
        for x in range(len(a)):
            n.append(m[0])
 #           print(n, 'pishu n')
 #           print(m, 'pishu m')
            if m[0] in cons:
  #              print(m[0], '-sogl')
                n.append("aig")
 #           print(n, 'pishu n')
            m = m[1:]
        o.append(('').join(n))
        n = []
 #       print(o)
    l = (' ').join(o)
    print(l)        
    
