import itertools
def solution(numbers):
        
    answer = set()

    arr = list(itertools.combinations(numbers,2))
    print(arr)
    
    for a in arr:
        answer.add(sum(a))
    
    answer = list(answer)
    answer.sort()

    return answer