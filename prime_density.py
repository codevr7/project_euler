# One of my Favourite pices of math
''' The fact that the prime frequency near a given number is very
        close to the natural log of that number'''

import math

def GetPrime(n_min):
    res = []
    for i in range(max(n_min,1), n_min + 1000):
        if IsPrime(i) == True:
            res.append(i)
    return 1000/len(res), math.log(n_min)

def IsPrime(n):
    for i in range(int(math.sqrt(n)), 1, -1):
        if n % i == 0 :
            return False
    return True
