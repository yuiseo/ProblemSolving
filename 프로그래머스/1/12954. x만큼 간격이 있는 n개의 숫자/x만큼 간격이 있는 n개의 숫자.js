function solution(x, n) {
    var answer = [];
    
    const add_x = x
    while (answer.length < n){
        answer.push(x)
        x+=add_x
    }
    
        
    return answer;
}