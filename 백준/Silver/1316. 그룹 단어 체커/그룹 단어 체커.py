import sys
input = sys.stdin.readline

n=int(input())

answer=0
for _ in range(n):
    word = input().rstrip()
    dict = {}

    # 앞 알파벳 저장 배열
    temp=''
    # 그룹 단어 체크 flag
    isCheck = True

    for w in word:
        if w not in dict:
            dict[w]=1

        else:
            dict[w]+=1
            if temp != w:
                isCheck = False
                break
            else:
                isCheck = True

        temp = w

    if isCheck:
        answer+=1

print(answer)