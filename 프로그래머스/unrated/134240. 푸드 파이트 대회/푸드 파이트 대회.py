def solution(food):
    answer = ''
    
    arr=[]
    for idx,val in enumerate(food):
        for i in range(val//2):
            arr.append(idx)
    
    for i in range(len(arr)):
        answer+=str(arr[i])
    
    answer+='0'
    
    for i in range(len(arr)-1,-1,-1):
        answer+=str(arr[i])

    return answer