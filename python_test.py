def lst(l):
    l = [[1],[2],[3]]
    for i in l:
        i.append(100)
        return l

print(lst([1,2,3,4]))
