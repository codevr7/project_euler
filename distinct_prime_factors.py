# A function for finding first "input" numbers to have "input" distinct primes
def con_dist_prime(con, diff):
    n = 3 ; dist_prime = [] # Initial values 
    while True: # While program running
        if is_dist_prime(n, diff): # If value has distinct prime factors
            curr = True
            dist_prime.append(n)
            if len(dist_prime) == con: # If "input" consecutive distincts found
                return dist_prime
        else :  # If not distinct ; Empty distinct primes
            curr = False
            dist_prime = []

        print(n, curr) # Finding current state for program
        n += 1


# A function that evaluates whether given number is a distinct prime
def is_dist_prime(num,times):
    fact = factor(num) ; fact_copy = [] # Initial value

    if is_prime(num) == True:
        return None
    
    # Finding prime-factors of given number
    for i in fact: # Iterate till list's last element
        if not is_prime(i):
            check = factor(i) # Add factors of non-prime to empty list
            fact.remove(i) # Empty the non-prime found in list
            fact.extend(check) # Add factors of non-prime to factor list

    # Removing factors from list which repeat more than once
    for j in fact:
        if j in fact_copy:# If element's repetition is more than once
            continue # Skip rest, go to next value
        fact_copy.append(j) # If no membership, add membership

    if len(fact_copy) == times:
        return True
    return False


# A function that returns a single factor of a given number
def factor(num):
    for i in range(int(num/2), 1, -1):
        if num % i == 0:# If current value divided by input gives no remainder 
            return [i,int(num / i)] # Return value and input by value

def is_prime(num):
    for i in range(int(num/2), 1, -1):
        if num % i == 0:
            return False
    return True

print(con_dist_prime(2,2))
