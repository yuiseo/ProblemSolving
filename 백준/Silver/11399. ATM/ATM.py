n = int(input())
people=list(map(int,input().split()))
people.sort()
answer=0
for i in range(n):
    answer+=people[i]*(n-i)

print(answer)