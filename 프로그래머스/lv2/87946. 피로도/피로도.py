from itertools import permutations
def solution(k, dungeons):
    answer = 0
    dungeons_N = len(dungeons)
    
    for permus in permutations(dungeons,dungeons_N):
        temp_k = k
        cnt=0
        for permu in permus:
            if permu[0] <= temp_k:
                temp_k -=permu[1]
                cnt+=1
            if answer < cnt:
                answer = cnt
    return answer