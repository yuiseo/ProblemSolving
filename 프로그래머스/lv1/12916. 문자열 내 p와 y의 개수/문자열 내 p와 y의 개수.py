def solution(s):
    answer = True
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    p_num,y_num=0,0
    new=s.upper()
    for i in range(len(s)):
        if new[i] == 'P':
            p_num+=1
        elif new[i] == 'Y':
            y_num+=1
    
    if p_num == y_num:
        return True
    elif p_num + y_num == 0:
        return True
    else:
        return False
