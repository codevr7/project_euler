import math

def prime_factor(num):
    factors = fact_pair(num)
    for i in factors:
        if is_prime(i) == False:
            factors.extend(prime_factor(i))
            factors.pop(factors.index(i))
    return factors

# Function which returns one factor pair of given number
def fact_pair(fact):
    for i in range(int(fact/2), 0, -1):
        if fact % i == 0:
            return [i, int(fact/i)]

# Function which returns whether given number was prime or non-prime
def is_prime(num):
    for i in range(2, int(math.sqrt(num))):
        if num % i == 0:
            return False
    return True 

print(prime_factor(123456720))
