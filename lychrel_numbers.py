# A function for returning number of lychrel numbers below given number
def num_val(val):
    length = 0 ; ret = [] # Variable for length of list and saving all lychrels
    for i in range(val, 0, -1):
        if is_lychrel(i): 
            ret.append(i) # Add i to lychrel list
            length += 1 # Add to length by 1
    return ret, length


# A function which returns whether input is lychrel
def is_lychrel(num):
    for i in range(50): 
        pal_sum = num + is_palindrome(num, True) # Sum of value and it's reverse
        if is_palindrome(pal_sum): # If sum is palindrome
            return False
        num = pal_sum  # Changing value to sum of value and it's palindrome
    return True # If no palindrome found after 50 iterations, number is lychrel


# A function for returning palindrome of input or whether input is palindrome
def is_palindrome(num, ret_palin=False):
    lst = [int(i) for i in str(num)] # Converting INT input to LIST
    lst_copy = lst[:] # Making copy of list for later comparision
    lst.reverse()

    if ret_palin: # If user specifies to return palindrome
        return int("".join(map(str,lst))) # Returning integer form of list

    for i in range(int(len(lst)/2)): # Checking if both indexes of lists match
        if lst[i] != lst_copy[i]: # If both indexes don't match
            return False
    return True
    
print(num_val(10000))
