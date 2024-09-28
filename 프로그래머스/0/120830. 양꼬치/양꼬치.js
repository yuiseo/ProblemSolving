function solution(n, k) {
    var answer = 0;
    if(n>=10){
        let free_drink = Math.floor(n/10)
        answer = n*12000 + 2000*(k-free_drink)
    } else {
        answer = n*12000 + 2000*k
    }
    return answer;
}