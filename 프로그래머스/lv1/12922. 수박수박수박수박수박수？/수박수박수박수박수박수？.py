def solution(n):
    answer = ''
    cnt=0
    while True:
        if cnt==n:
            break
            
        if cnt%2==0:
            answer+='수'
        else:
            answer+='박'
        cnt+=1
    return answer