def solution(citations):
    citations = sorted(citations)
    index = len(citations)
    for i in range(index):
        if citations[i]>=index-i:
            return index-i
    return 0

#     citations.sort(reverse=True) 
#     for idx,val in enumerate(citations):
#         if idx >= val:
#             return idx
#         print(idx,val)
#     return len(citations)
    