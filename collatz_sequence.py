'''Given a number if its odd multiply by 3 and add 1 ,if its even divide by two
   and if its one just return 1. 
        Continue the same process with the resulting numbers.
            The collatz conjecture says every number ends up in 1 by
            applying this process'''
# The collatz sequence

def collatz(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return collatz(n/2)
    else:
        return collatz((3 * n) + 1)
print(collatz(10380))
