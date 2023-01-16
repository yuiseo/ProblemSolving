def solution(x, n):
    answer = []
    answer.append(x)
    while True:
        if n==1:
            break
        answer.append(answer[-1]+x)
        n-=1
    return answer