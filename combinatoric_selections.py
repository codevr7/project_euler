'''https://projecteuler.net/problem=53 '''
# Go to above URL to understand problem
 
# Returns all possible combinatorics above given limit till hundred
def selections(limit):
    sel = 0    
    for i in range(23,101):
        for j in range(1,i):
            # If iterating(i,j) form combinatoric(i,j) above limit
            if combinatoric(i,j) > limit: 
                sel += 1 # Adds to selectiions
        continue
    return sel

# Returns combinatoric of given values
def combinatoric(n,r):
    # Equation for combinatoric pair
    comb = factorial(n)/(factorial(r) * factorial(n - r)) 
    return int(comb)

# Returns factorial of given number
def factorial(n):
    prod = n
    for i in range(n - 1, 1, -1):
        prod *= i 
    return prod

print(selections(1000000))
