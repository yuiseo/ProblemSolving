import math
def is_prime(x):
    if x == 1:
        return False
    else:
        for i in range(2,int(math.sqrt(x))+1):
            if x % i == 0:
                return False
        return True
    
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if is_prime(i):
            answer+=1
            
    return answer