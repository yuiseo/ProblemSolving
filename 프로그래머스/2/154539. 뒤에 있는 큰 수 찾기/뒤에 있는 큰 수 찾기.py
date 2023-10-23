def solution(numbers):

    
#   시간 초과 - 82.6점
#     answer = [-1]*len(numbers)
#     for i in range(len(numbers)):
#         for j in range(i,len(numbers)):
#             if numbers[i] < numbers[j]:
#                 answer[i] = numbers[j]
#                 break

    answer = [-1]*len(numbers)
    # stack 활용
    stack = []
    
    for i in range(len(numbers)):
        target = numbers[i]

        while stack and numbers[stack[-1]] < target:
            answer[stack.pop()] = target
        
        stack.append(i)
 
           
    return answer