def primes_by_six(limit):
    sexy_primes = []
    primes = all_primes(limit)
    for i in primes:
        if (i + 6) in primes:
            sexy_primes.append([i,i + 6])
    return sexy_primes


# Returns all primes below or equal to a given number
def all_primes(n):
    List = []
    for i in range(2, n + 1):
        if is_prime(i) == True:
            List.append(i)
    return List

# Evaluates whether given number is prime or not
def is_prime(n):
    for i in range(int(n/2), 1, -1):
        if n % i == 0:
            return False
    return True

print(primes_by_six(100))
