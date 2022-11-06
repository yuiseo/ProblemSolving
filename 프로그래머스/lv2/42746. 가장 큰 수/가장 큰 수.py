from itertools import permutations
def solution(numbers):
    answer=0
    numbers = list(map(str,numbers))
    numbers.sort(key = lambda x : x*3, reverse=True)
    
    return str(int(''.join(numbers)))
    
#     answer = ''
#     max_val = 0
#     num = len(numbers)
#     numbers = list(permutations(numbers,len(numbers)))
    
#     arr = []
#     for i in range(len(numbers)):
#         temp=''
#         for j in range(num):
#             temp+=str(numbers[i][j])
        
#         arr.append(temp)
#     arr.sort(reverse=True)
            
#     answer = arr[0]
#     return answer