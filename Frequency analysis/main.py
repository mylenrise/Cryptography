def createDictlist():
    s = 97
    dictlist = {}
    for i in range(26):
        dictlist[chr(s)] = 0
        s += 1
    return dictlist


def coincidenceInd(t):
    dictlist = createDictlist()
    f = open('inf.txt', 'r')
    symbCount = 0
    check = t
    for str in f:
        for symbol in str:
            if symbol != ' ':
                if check == t:
                    symbCount += 1
                    dictlist[symbol] += 1
                    check = 1
                else:
                    check += 1

    index = 0
    for symbol in dictlist:
        index += (dictlist[symbol] * (dictlist[symbol] - 1)) / (symbCount * (symbCount - 1))

    return index


def findKey(start, period):
    dictlist = createDictlist()
    f = open('inf.txt', 'r')
    symbCount = 0
    check = period - start
    for str in f:
        for symbol in str:
            if symbol != ' ':
                if check == period:
                    symbCount += 1
                    dictlist[symbol] += 1
                    check = 1
                else:
                    check += 1
    mostlyUsed = ''
    temp = 0
    for symbol in dictlist:
        if dictlist[symbol] > temp:
            mostlyUsed = symbol
            temp = dictlist[symbol]
    if ord(mostlyUsed) - 101 < 0:
        return 26 + ord(mostlyUsed) - 101
    else:
        return ord(mostlyUsed) - 101


def decryptText(keylist, keylen):
    f = open('inf.txt', 'r')
    fout = open('out.txt', 'w')
    keyInd = 0
    for str in f:
        for symbol in str:
            if symbol != ' ':
                if ord(symbol) - keylist[keyInd] < 97:
                    fout.write(chr(122 + (ord(symbol) - 96 - keylist[keyInd])))
                else:
                    fout.write(chr(ord(symbol) - keylist[keyInd]))
                keyInd += 1
                if keyInd == keylen:
                    keyInd = 0
            else:
                fout.write(' ')


keyLen = 0
maxInd = 0

for i in range(2, 30):
    temp = coincidenceInd(i)
    if temp > maxInd:
        maxInd = temp
        keyLen = i

keylist = []

for i in range(keyLen):
    keylist.append(findKey(i, keyLen))
decryptText(keylist, keyLen)
