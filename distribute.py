def line_pascal(line):
    pascal_list = [1,1] # Initial line in pascal's triangle
    for i in range(line - 1):
        pascal_list = pascal(pascal_list)
    return pascal_list

# Returns list after completing given pascal computation for given list
def pascal(line):
    res = [line[0]]
    for i in range(1,len(line)):
        res.append(line[i] + line[i - 1])
    res.append(line[-1])
    return res

print(line_pascal(4))
