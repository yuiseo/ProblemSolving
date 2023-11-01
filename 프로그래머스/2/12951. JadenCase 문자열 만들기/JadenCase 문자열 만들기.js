function solution(s) {
    var answer = '';
    arr = s.split(' ').map((item)=>item.charAt(0).toUpperCase() + item.slice(1).toLowerCase())
    
    answer = arr.join(' ')
    return answer;
}