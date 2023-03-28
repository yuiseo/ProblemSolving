def solution(k, tangerine):
    answer = 0
    d = dict()
    
    for i in list(set(tangerine)):
        d[i]=0
    for t in tangerine:
        d[t]+=1
    
    new = sorted(d.items(),key=lambda x:x[1], reverse=True)
    for n in new:
        if k>0:
            k-=n[1]
            answer+=1
        else:
            break
        
        
    return answer