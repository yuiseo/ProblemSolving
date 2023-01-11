n,m = map(int,input().split())

site = dict()
for i in range(n):
    name,pw = map(str,input().split())
    site[name]=pw

for j in range(m):
    find = input()
    print(site[find])