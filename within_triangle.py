from fractions import Fraction

def within_tri(vert_1, vert_2, vert_3, Point):
    # Calculates slope of each line in given triangle
    slope_1 = (vert_2[1] - vert_1[1]) / (vert[0] - vert[0])
    slope_2 = (vert_3[1] - vert_2[1]) / (vert_3[0] - vert_2[0])

def within_line(start, end, Point):
    slope = (end[1] - start[1]) / (end[0] - start[0])
    slope = Fraction(slope)
    curr_val = start  # Assigns chaniging variable 
    while curr_val != end: 
        curr_val = (curr_val[0] + 1, curr_val[1] + slope)
        print(curr_val)
        if curr_val == Point:
            return True
    return False

#print(within_line((1,4), (6,1), (4,5)))
print(within_line((1,1), (5,5), (4,4)))
