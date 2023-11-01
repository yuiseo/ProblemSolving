function solution(s) {
    var answer = '';
    
    arr = s.split(' ').map((item)=>Number(item))
    const maxValue = Math.max(...arr)
    const minValue = Math.min(...arr)
    
    answer+=minValue
    answer+=' '
    answer+=maxValue
    
    return answer;
}