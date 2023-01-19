import sys
input = sys.stdin.readline
n = int(input())

#딕셔너리 생성
birth={}
for _ in range(n):
    #공백 제거를 위해 strip()
    #이름,일,월,년
    name,d,m,y = map(str,input().strip().split(' '))
    #한자리 수 앞에 0붙이기
    if len(d)==1:
        d='0'+d
    if len(m)==1:
        m='0'+m
    #딕셔너리에 추가
    birth[name] = int(y+m+d)

#출생년도가 느린 순으로 정렬
sort_birth = sorted(birth.items(),key=lambda x:x[1],reverse=True)

#나이가 가장 어린 사람
print(sort_birth[0][0])
#나이가 가장 많은 사람
print(sort_birth[-1][0])