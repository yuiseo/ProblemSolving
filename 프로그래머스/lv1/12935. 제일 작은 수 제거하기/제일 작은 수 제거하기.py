def solution(arr):
    answer = []
    
    min_N=min(arr)
    arr.remove(min_N)
    
    if len(arr)==0:
        answer.append(-1)
        return answer
    else:
        return arr