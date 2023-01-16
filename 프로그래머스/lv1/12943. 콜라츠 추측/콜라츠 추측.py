def solution(num):
    answer = 0
    
    cnt=0
    while True:
        if num == 1:
            break
        if cnt>500:
            answer = -1
            break
            
        if num%2 == 1:
            num=num*3+1
        else:
            num=num//2
        answer+=1
        cnt+=1
    return answer