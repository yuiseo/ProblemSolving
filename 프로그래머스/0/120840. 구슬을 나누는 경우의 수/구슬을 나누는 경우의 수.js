function solution(balls, share) {
    // BigInt를 사용하여 팩토리얼을 계산
    function factorial(n) {
        return n === 0 ? BigInt(1) : BigInt(n) * factorial(n - 1);
    }

    // 조합 공식: n! / (r! * (n - r)!)
    const answer = factorial(balls) / (factorial(share) * factorial(balls - share));
    
    return Number(answer);  // BigInt를 다시 숫자로 변환하여 반환
}