# Returns the largest ratio of 'n' and 'psi(n)' for all 'n' below given input
def num_by_psi(value):
    largest = 0
    for i in range(2, value + 1):
        print(i)
        curr = psi(i)
        if i/curr > largest:
            largest = i/curr
            num = i
    return (largest,num)


# Euler's totient function
# Returns all values below input which are relatively prime to it
def psi(n):
    ret = 1
    for i in range(2, n):
        if relative_prime(i,n) == False:
            ret += 1
    return ret


# Returns if given inputs are relatively prime
def relative_prime(a,b):
    if b % a == 0:
        return True
    for i in range(2, int(a/2) + 1):
        if a % i == 0 and b % i == 0:
            return True
    return False

print(num_by_psi(1000000))
