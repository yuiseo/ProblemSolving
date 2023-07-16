import sys
input = sys.stdin.readline

n = int(input())
#dictionary로 풀이
company = {}

for _ in range(n):
    person,log = map(str,input().split(' '))
    if log == 'enter\n':
        company[person] = True
    else:
        del company[person]

answer = sorted(company,reverse=True)

for a in answer:
    print(a)
    
#list로 풀이

#company = []
# arr = [input().split(' ') for _ in range(n)]
#
# for a in arr:
#     if a[1] == 'enter\n':
#         company.append(a[0])
#     else:
#         idx = company.index(a[0])
#         company.pop(idx)
#
# company.sort(reverse=True)
# for c in company:
#     print(c)