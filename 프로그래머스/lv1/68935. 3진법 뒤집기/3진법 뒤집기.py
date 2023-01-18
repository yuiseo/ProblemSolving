def solution(n):
    #10진법을  3진법으로 변환
    temp=''
    while n:
        temp+=str(n%3)
        n=n//3
    
    #3진법을 10진법으로 변환
    n = int(temp,3)

    return n