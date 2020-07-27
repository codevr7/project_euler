def sqrt(num, digits=5):
    # Initial Values
    sqrt = binary_search(num) # Fetches range which square root lies
    place_val = 1
    
    # Range for tracking neccessary digits
    for j in range(digits):
        place_val /= 10 
        Break = False 
        for i in range(9, 0, -1):
            if Break:
                continue
            curr = (sqrt + (place_val * i)) # Increases current value 
            if curr ** 2 < num: # If check squared reduces below given number
                sqrt = curr
                Break = True
            if curr ** 2 == num:
                return curr, curr ** 2
    return sqrt, sqrt ** 2 

    
# Returns between which pair of digits does input's square root lie
def binary_search(num):
    lower =  False

    # Evaluates whether given number's square root is more or less than 4
    if num > 25:
        var = int(num/4)
    if num <= 25:
        var = num
    
    # Executes binary search
    higher = var
    while not lower:
        if (higher - 1)**2 < num:
            lower = higher - 1
            break
        else:
            higher -= 1
    return (lower)

print(sqrt(16.3,4))
