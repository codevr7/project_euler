def luhn(string):
    l = []
    for j in range(1,len(string) + 1):
        for i in string:
            print(i)
            if j % 2 == 0 :
                l.extend(Break(j))
            else:
               l.append(j)
    Sum = sum(l)
    if Sum % 10 == 0:
        return str ("Verified")
    return str ("Invalid code")

def Break(string):
    l = []
    for i in string:
        l.append(int(i)*2)
    return l

print(luhn("1762483"))
