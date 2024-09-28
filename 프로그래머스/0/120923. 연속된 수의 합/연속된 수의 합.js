function solution(num, total) {
    // 연속된 수의 첫 번째 숫자를 구하는 공식
    // x, x+1, x+2, x+3, ... x+(num-1)
    // num * x + num * (num-1) / 2 => 연속된 수의 합
    // num(x+(num-1)/2) = total
    // total / num = x + (num-1)/2
    // x = (total - (num*(num-1)/2))/num
    let start = (total - (num * (num - 1) / 2)) / num;
    let answer = [];

    // start부터 시작해서 num개의 숫자를 배열에 담기
    for (let i = 0; i < num; i++) {
        answer.push(start + i);
    }

    return answer;
}
