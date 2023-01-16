def solution(n):
    answer = []
    num = str(n)
    for i in range(len(num)):
        answer.append(num[i])
    answer.sort(reverse=True)
    
    num_str=''
    for i in range(len(answer)):
        num_str+=answer[i]
    
    return int(num_str)
    