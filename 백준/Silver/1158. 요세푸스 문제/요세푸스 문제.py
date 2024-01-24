import sys
input = sys.stdin.readline

N, K = map(int, input().split())
answer = []

queue = []
for i in range(1, N + 1):
    queue.append(i)

idx = 0

while queue:
    idx = (idx + K - 1) % len(queue)
    answer.append(queue.pop(idx))

print("<" + ", ".join(map(str, answer)) + ">")
