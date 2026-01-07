function solution(numbers) {
    var answer = ''
    const strNumbers = numbers.map((number)=>number+'')
    // strNumbers.sort((a, b) => (b + a).localeCompare(a + b));
    
    strNumbers.sort((a,b)=>{
        const ab = a+b
        const ba = b+a
        return ba>ab?1:-1
    })
    
    if (strNumbers[0] === "0") return "0";
    answer = strNumbers.join('')
    return answer;
}