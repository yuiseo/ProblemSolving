def solution(s):
    answer = ''
    
#     arr = list(map(str,s.split(' ')))
    
#     for i in range(len(arr)):
#         temp = arr[i].lower()
#         answer+=temp[0].upper()
        
#         for j in range(1,len(arr[i])):
#             answer+=temp[j]
#         if i != len(arr)-1:
#             answer+=' '
    
    s=s.split(' ')
    for i in range(len(s)):
        # 첫글자 대문자로
        s[i]=s[i].capitalize()
    #공백을 join으로 연결
    answer=' '.join(s)
    
    return answer