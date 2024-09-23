function solution(dots) {
    var answer = 0;
    // 평행하려면 기울기 같아야 함
    // 기울기 = y증가량 / x 증가량
    const [[x0,y0],[x1,y1],[x2,y2],[x3,y3]] = dots
    
    // 0&1 2&3
    if((y0-y1) / (x0-x1) === (y2-y3) / (x2-x3)) return 1
    
    // 0&2 1&3
    if((y0-y2) / (x0-x2) === (y1-y3) / (x1-x3)) return 1
    
    // 0&3 1&2
    if((y0-y3) / (x0-x3) === (y1-y2) / (x1-x2)) return 1
    
    
    return answer;
}