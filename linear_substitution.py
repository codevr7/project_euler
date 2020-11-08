# Returns the values of a linear equation
def sle(val_1, val_2):
    if not similar_equation(val_1, val_2):
        return False

    # The numerator and denominator for the variable 'y'
    num = (val_1[2] * val_2[0]) - (val_1[0] * val_2[2])
    den = (val_1[1] * val_2[0]) - (val_1[0] * val_2[1])
    y = num/den
    x = (val_1[2] - (val_1[1] * y))/val_1[0] 
    return (x,y)

# Checks whether given equations are similar
def similar_equation(l1, l2):
    if l1[0]/l2[0] == l1[1]/l2[1]:
        return False
    return True

print(sle([2, 3, 13], [5, -1, 7]))
