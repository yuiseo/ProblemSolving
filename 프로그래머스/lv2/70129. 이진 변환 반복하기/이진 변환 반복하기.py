def solution(s):    
    zero = 0
    con = 0
    
    while s!='1':
        
        if '0' in s:
            #0 개수 더해주기
            zero += s.count('0')
            #0 제거
            s = s.replace('0','')
        
        #0을 뺀 길이
        length = len(s)
        #2진 변환
        s = str(format(length,'b'))
        #변환 횟수
        con +=1
        

    return [con,zero]