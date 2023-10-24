def solution(land):
    if len(land) == 1:
        return max(*land)
    
    # i 행, j 열
    for i in range(1, len(land)):
        for j in range(4):
            land[i][j] += max(land[i-1][:j] + land[i-1][j+1:])
    return max(land[len(land)-1])