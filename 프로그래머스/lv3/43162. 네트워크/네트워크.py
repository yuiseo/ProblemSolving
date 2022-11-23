from collections import deque
def solution(n, computers):
    
    def BFS(i):
        queue=deque()
        queue.append(i)
        
        while queue:
            now = queue.popleft()
            #방문 체크
            visit[now] = 1
            
            for i in range(n):
                if not visit[i] and computers[now][i]:
                    queue.append(i)
        print(visit)
        
    answer = 0
    # visit 배열을 잘못 만들었었음.. 바보..
    visit = [0]*n
    for i in range(n):
        #방문한 적이 없으면
        if not visit[i]:
            BFS(i)
            answer+=1
    return answer