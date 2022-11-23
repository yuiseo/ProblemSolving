# stack 활용
# 처음에 bfs로 시도했지만, bfs로 풀다보면 출발점이 같을 때 목적지가 여러곳일 경우가 있어
# 예외처리 하기 힘이든다,,
# 대부분의 풀이들은 dfs 또는 stack을 활용..

def solution(tickets):
    answer = []
    # stack을 활용하기 위해 역순으로 sort (문제의 조건 : 알파벳 순)
    tickets.sort(reverse=True)
    route = dict()
    for st,ed in tickets:
        # dict에 있는 경우
        if st in route:
            route[st].append(ed)
        #value를 list로 만든다
        else:
            route[st] = [ed]
    print(route)
        
    # stack
    stack = ['ICN']
        
    while stack:
        now = stack[-1]

        # now가 route에 없거나 route(목적지)가 비었을 경우
        if now not in route or len(route[now])==0:
            answer.append(stack.pop())
        else:
            stack.append(route[now].pop())
    # stack으로 빼줬기 때문에 다시 reverse
    answer.reverse()
    return answer