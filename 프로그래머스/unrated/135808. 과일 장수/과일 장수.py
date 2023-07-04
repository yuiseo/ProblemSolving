def solution(k, m, score):
    answer = 0
    
    # 점수 높은순으로 정렬
    score.sort(reverse=True)
    # 최대 사과점수 k
    apple=[x for x in score if x<= k]
    
    # 한상자에 m개씩 자르기
    for i in range(0,len(apple),m):
        temp = apple[i:i+m]
        
        # m개일 경우에만 상자로
        if len(temp) == m:
            answer+=min(temp)*m

    
    return answer