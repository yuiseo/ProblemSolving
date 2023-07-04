def solution(name, yearning, photo):
    answer = []
    dict={}
    
    ## name과 그리움 점수를 dictionary에 저장
    for i in range(len(name)):
        dict[name[i]] = yearning[i]
    
    ## 일치하는 키값만 그리움 점수 더해서 answer에 더해줌
    for i in range(len(photo)):
        point = 0
        for j in range(len(photo[i])):
            if photo[i][j] in dict:
                point+=dict[photo[i][j]]
        answer.append(point)
    return answer