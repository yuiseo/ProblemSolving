function solution(numbers) {
    var answer = ''
    const strNumbers = numbers.map((number)=>number+'')
    strNumbers.sort((a, b) => (b + a).localeCompare(a + b));
    if (strNumbers[0] === "0") return "0";
    answer = strNumbers.join('')
    return answer;
}