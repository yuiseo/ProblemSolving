def solution(n, left, right):
    answer = []
    
    # 사각형의 원리
    # 첫번째 지점을 (1,1)이라 생각했을 때 y,x중 max값이 해당 자리의 값
    # 따라서 해당 자리의 값을 알려면 y,x의 max값을 찾아야함
    # index는 0부터 시작하니 +1 해서 answer에 추가
    for i in range(left, right+1):
        answer.append(max(i//n,i%n)+1)
        
    return answer