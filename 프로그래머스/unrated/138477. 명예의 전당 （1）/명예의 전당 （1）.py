def solution(k, score):
    answer = []
    
    best=[]
    for s in score:
        best.sort(reverse=True)
        if len(best)>=k:
            if min(best)<s:
                best.pop()
                best.append(s)
        else:
            best.append(s)
        answer.append(min(best))
    return answer