function solution(emergency) {
    var answer = [];
    
    // 배열 복사!
    const sorted_emergency = [...emergency].sort((a, b) => b - a)
    
    emergency.map((n)=>{
        answer.push(sorted_emergency.indexOf(n)+1)
    })

    return answer;
}