def solution(cards1, cards2, goals):
    
    for goal in goals:
        if cards1 and goal == cards1[0]:
            cards1.pop(0)
        elif cards2 and goal == cards2[0]:
            cards2.pop(0)
        else:
            return 'No'
    
    return 'Yes'