function solution(numbers, num1, num2) {
    var answer = [];
    numbers.forEach((number,idx)=>{
        if(idx>=num1 && idx<=num2){
            answer.push(number)
        }
    })
    return answer;
}