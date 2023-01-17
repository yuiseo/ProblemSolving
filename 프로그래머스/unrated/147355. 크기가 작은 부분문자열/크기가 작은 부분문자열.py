def solution(t, p):
    answer = 0
    
    for i in range(len(t)):
        if len(t[i:i+len(p)])==len(p) and int(t[i:i+len(p)])<=int(p):
            answer+=1
    return answer