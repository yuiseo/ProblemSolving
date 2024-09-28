function solution(age) {
    var answer = '';
    
    age.toString().split('').forEach((s)=>{
        answer += String.fromCharCode(parseInt(s)+97)
    })
    return answer;
}