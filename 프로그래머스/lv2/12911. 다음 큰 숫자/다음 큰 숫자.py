def solution(n):
    answer = 0
    
    cnt = bin(n).count('1')
    answer = n+1
    
    while answer < 1000000:
        if bin(answer).count('1')==cnt:
            break
        answer+=1

    return answer