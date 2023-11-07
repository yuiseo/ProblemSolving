function solution(n) {
    
    // 2진수 변환
    let bin = n.toString(2)
    // 다음 큰 수의 1 개수
    let one = bin.split('1').length
    
    while(true){
        n++
        if(n.toString(2).split('1').length === one) return n
    }
}