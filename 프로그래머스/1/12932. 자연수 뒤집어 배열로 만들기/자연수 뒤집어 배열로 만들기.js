function solution(n) {
    var answer = [];
    
    n = String(n)
    arr = (n.split('')).reverse()
    answer = arr.map((item)=>Number(item))
    
    return answer;
}