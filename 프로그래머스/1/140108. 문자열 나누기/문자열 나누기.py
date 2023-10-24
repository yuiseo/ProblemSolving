def solution(string):
    answer = 0
    
    x_cnt, nx_cnt = 0,0
    for s in string:

        if x_cnt == nx_cnt:
            answer+=1
            x = s
        if x == s:
            x_cnt+=1
        else:
            nx_cnt+=1
        
        
    return answer