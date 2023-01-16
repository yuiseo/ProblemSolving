def solution(s):
    answer = ''
    
    if len(s)%2==1:
        idx = len(s)//2
        answer+=s[idx]
    else:
        idx=len(s)//2
        answer+=s[idx-1:idx+1]
    return answer