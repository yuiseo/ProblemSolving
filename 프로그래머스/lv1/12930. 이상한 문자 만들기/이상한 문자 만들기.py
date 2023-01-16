def solution(s):
    answer = ''
    
    arr=list(map(str,s.split(' ')))
    print(arr)
    
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if j%2==0:
                answer+=arr[i][j].upper()
            else:
                answer+=arr[i][j].lower()
        if i != len(arr)-1:
            answer+=' '

    return answer