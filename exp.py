import math

# Returns value of e raised to x of a given value
def exp(x): 
    res = 0
    for i in range(100):
        res += (x ** i/math.factorial(i)) 
    return res

print(exp(math.log(2)/2))
print(exp(2) * exp(3))
