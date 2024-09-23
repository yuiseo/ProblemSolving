function solution(array) {
    var answer = 0;    
    array.sort((a, b) => a - b);
    
    const target_idx = parseInt(array.length/2)

    answer = array[target_idx]

    return answer;
}