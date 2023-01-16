def solution(x):
    answer = True
    
    new_x = str(x)
    add_x=0
    for i in range(len(new_x)):
        add_x += int(new_x[i])
    
    if x % add_x == 0:
        answer = True
    else:
        answer = False
    return answer