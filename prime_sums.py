import math

# A function for returning number containing largest prime sum upto given value
def largest_prime_sum(val):
    prime_sums = [] ; comp_largest = []
    largest = [0,0] # Initial largest
    if val % 2 != 0: # If input even, setting initial as odd
        val -= 1

    for i in range(val - 1, 2, -2): # Range from initial to 1,skipping even 
        if is_prime(i) == False:  continue # If current is non-prime, skip loop
        # If prime-sums of value are more than largest, value becomes largest
        if len_prime_sum(i) > largest[1]: 
            largest = [i, len_prime_sum(i)]
    return largest


# A function for finding if input is a sum of primes
def len_prime_sum(val_sum):
    prime_sum = cons_prime_sum(val_sum) # Finding closest prime sums
    pop_left = prime_sum[:] # Copy for popping 1st element of prime sum until 
    pop_right = prime_sum[:] # Similar to last line but pops last element
    # Variables for tracking sum of list
    left_sum ,right_sum = sum(prime_sum),sum(prime_sum)

    if sum(prime_sum) == val_sum:
        return len(prime_sum)

    while left_sum > val_sum: # Until sum of primes is more than input
        left_sum -= pop_left[0]
        pop_left.pop(0) # Popping first element
        if left_sum  == val_sum:
            return len(pop_left)
        
    while right_sum  > val_sum:
        right_sum -= pop_right[-1]
        pop_right.pop(-1) # Popping last element
        if right_sum  == val_sum:
            return len(pop_right)
    return 0 # Return 0 if no prime present in sum


# A function for returning the sum of consecutive primes sums upto given value
def cons_prime_sum(val):
    prime_lst = [2] ; curr = 3 ; sum_lst = 2 
    # Until sum of primes greater or equal to input
    while sum_lst < val:
        if is_prime(curr) == True: # If value prime
            prime_lst.append(curr)
            sum_lst += curr
        curr += 2
    return prime_lst


def is_prime(n):
    for i in range(math.floor(math.sqrt(n)), 1, -1):
        if n % i == 0:
            return False
    return True

print(largest_prime_sum(1000))
