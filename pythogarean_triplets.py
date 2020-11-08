import math

# Returns all pythogarean triplets till given input
def allPythogarean(limit):
    triplets = []
    for i in range(1, limit + 1):
        for j in range(i, limit + 1):
            if isPythogarean(i,j, int(math.sqrt(i**2 + j**2))):
                triplets.append((i,j))
    return triplets

# Evaluates if given triple is a pythogarean triple
def isPythogarean(a,b,c):
    if a**2 + b**2 == c**2:
        return True
    else:
        return False

print(allPythogarean(100))
