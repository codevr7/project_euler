# A function that checks whether given value all have same digits
def permuted_multiples(times):
    n = 10
    comp = 0
    while True:
        mult_lst = [n*i for i in range(2,times + 1)]
        if check_permute(mult_lst) == False:
            n += 1 ; continue
        return n

def check_permute(lst):
    for i in lst[1:]:
        if is_digits(lst[0],i) == False:
            return False
    return True

def is_digits(inp_1, inp_2):
    # Converting given number to list of digits of the given number
    inp_1 ,inp_2= list(map(int, str(inp_1))), list(map(int, str(inp_2)))
    max_lst = (inp_1 if len(inp_1) > len(inp_2) else inp_2)

    for i in max_lst:
        if inp_1.count(i) != inp_2.count(i):
            return False
    return True

print(permuted_multiples(6))
