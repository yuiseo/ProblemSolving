def solution(babbling):
    answer = 0
    say = ["aya","ye","woo","ma"]
    
    for babble in babbling:
        for s in say:
            
            # 연속이지 않을 때
            if s*2 not in babble:
                #말 할 수 있는 단어 공백 처리
                babble = babble.replace(s,' ')
                
        if babble.isspace():
            answer+=1
    return answer