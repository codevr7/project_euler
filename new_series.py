# A function for returning the first "input" lines
def series(lines):
    lst = [[1]]
    while len(lst) != lines: # Unless length of list is length of input
        # Calling 2nd function and appending output to list
        lst.append(line_for_arg(len(lst) + 1))  
    return lst


# A function for returning the line according to given input
def line_for_arg(line):
    lst = [line]

    for i in range(line + 1, line * 2):
        lst.append(i)
    for j in range(line * 2 - 2, line - 1, -1):
        lst.append(j)
    return lst

print(series(4))
