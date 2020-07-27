def e(slits, base=False, parts=False):
    if not base or not parts:
        base,parts = slits,slits

    compounded_sum = 2
    for i in range(1,parts):
        val = 1/slits * i/base
        compounded_sum += val
        if i > 1:
            compounded_sum += (e(slits * base,base,i)) - 2
    return compounded_sum


print(e(4))

