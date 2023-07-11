import math
def solution(arr):
    answer = arr[0]
    
    #최소공배수 = 두수의 곱 // 최대공약수
    for number in arr:
        answer = answer*number//math.gcd(answer,number)
        
    return answer