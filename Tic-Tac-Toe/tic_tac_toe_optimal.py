import tic_tac_toe_result as result

def next_win(l1,l2,l3,val):
    indices = result.locations([l1,l2,l3],' . ')
    for i in range(1, 10):
        if i not in indices:
            continue 
        if i < 4:
            swp = l1
            replace(swp,i - 1,val)
            if result.check_win(swp,l2,l3,val):
                return i
        elif i < 7:
            swp = l2
            replace(swp,i - 4,val)
            if result.check_win(l1,swp,l3,val):
                return i
        else:
            swp = l3
            replace(swp,i - 7,val)
            if result.check_win(l1,l2,swp,val):
                return i
    return False
    
def replace(List,index,ele):
    del List[index]
    List.insert(index,ele)
    return List

print(next_win([' X ',' . ',' X '],[' X ',' O ',' O '],[' X ',' O ', ' X '],' X '))
