def solution(s):
    answer = 1
    
    if len(s)%2==1: return 0
    if len(s)==2:
        if s[0] == s[1]: return 1
    
    arr = list(s)
    stack = [arr.pop(0)]
    
    for a in arr:
        if len(stack)>0 and stack[-1]==a:
            stack.pop()
        else:
            stack.append(a)
    if len(stack):
        answer=0
    return answer