def solution(n):
    arr = [i for i in range(1,n+1)]
    answer = 0
    start = 0
    end = 0

    # start가 n보다 작을때까지만
    while start < n:
        if sum(arr[start:end])<n:
            end+=1
        
        elif sum(arr[start:end])>n:
            start+=1
        
        else:
            answer+=1
            start+=1
            end+=1
    
    return answer