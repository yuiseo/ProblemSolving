from collections import Counter
# zip
# 두 개의 서로 다른 리스트에서 하나를 key로 하고 다른 하나를 value로 해서 딕셔너리로 표현할 때 사용

# Counter
# 컨테이너안의 데이터를 편리하고 빠르게 개수를 세도록 지원
def solution(want, number, discount):
    answer = 0
    
    # 원하는 것과 갯수를 딕셔너리로 변환
    want_dict = {}
    for w,n in zip (want, number):
        want_dict[w]=n
    
    # 10일이 기준이기 때문에 -9
    for i in range(len(discount)-9):
        # 할인 품목 딕셔너리로 변환
        discount_dict = Counter(discount[i:i+10])
        # 같을 때의 가능한 일 반환
        if want_dict == discount_dict:
            answer+=1
        
    return answer