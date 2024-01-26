n = int(input())
for i in range(n):
    lst = list(map(str,input().split()))
    for j in range(len(lst)):
        print(lst[j][::-1],end=' ')