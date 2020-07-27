# A function that returns the largest product of a given number's sums
def largest_split(num):
    largest = 0
    for i in sum_pair(num): # Iterating through all the sums of given number
        mult = 1
        for j in i: # Iterating through current list value
            mult *= j
        if mult > largest:
            largest = mult
    return largest

# A function that returns all the possible sums of a given number
def sum_pair(num):
    ret = []
    for i in range(2,num - 1):
        # If value smaller than 5 don't break as it's sum's product isn't bigger
        if i < 5: 
            ret.append([num - i, i])
            continue
       # if i > 4:
        for j in sum_pair(i): # Using recursion to break further
            j.insert(0,num - i)
            ret.append(j)
    return ret

                
print(largest_split(10))

