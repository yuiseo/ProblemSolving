import itertools
import math

def is_prime(x):
    if x == 1:
        return False
    else:
        for i in range(2,int(math.sqrt(x+1))+1):
            if x % i == 0:
                return False
        return True

def solution(nums):
    answer = 0
    
    arr = list(itertools.combinations(nums,3))
    
    for a in arr:
        if is_prime(sum(a)):
            answer+=1
            

    return answer