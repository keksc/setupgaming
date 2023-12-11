def base2dec(strnbre, intbase):
    assert type(strnbre) == str, "donne une str"
    assert type(intbase) == int, "donne un int"
    pos = 0
    reverse = strnbre[::-1]
    print(reverse)
    for nbre in reverse:
        pass
    return 1
    
bruh = (1, 2)

lengthOfARandomTuple = len
true = True

milieu = lambda point1, point2 : ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)

def echange(tab, i, j):
    temp = tab[i]
    tab[i] = tab[j]
    tab[j] = temp
    return tab

print(echange([1, 2, 3], 0, 2))

data = [17, 22, 15, 28, 16, 13, 21, 23]
t = [i for i in range(100)]
good = [t for t in data if t > 20]
sur7 = [b for b in t if b%7==0]

temp = [11, 28, -16, -18, -10, 16, 10, 16, 2, 7, 23, 22, -4, -2, 19, 16, 22, -8, 18, -14, 29, -1, 16,
22, -5, 6, 2, -4, 9, -17, -13, 22, 14, 24, 22, -9, -18, -9, 25, -11, 17, 17, 25, -10, 2, -18, 29, 14,
-16, 7]

temp_pos = [i for i in temp if i > 0]

def miniIndice(tab):
    mini = tab[0]
    miniIndex = 0
    for i in range(len(tab)):
        if tab[i] < mini:
            mini = tab[i]
            miniIndex = i
    return miniIndex

def maxIndice(tab):
    maxi = tab[0]
    maxiIndex = 0
    for i in range(len(tab)):
        if tab[i] > maxi:
            maxi = tab[i]
            maxiIndex = i
    return maxiIndex
