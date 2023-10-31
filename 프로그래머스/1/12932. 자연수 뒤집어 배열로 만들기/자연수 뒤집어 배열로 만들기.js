function solution(n) {
    var answer = [];
    
    n = String(n)
    answer = (n.split('')).reverse().map((item)=>Number(item))
    
    return answer;
}