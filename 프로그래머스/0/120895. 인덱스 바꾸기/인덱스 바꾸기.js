function solution(my_string, num1, num2) {
    let arr = my_string.split('');
    [arr[num1], arr[num2]] = [arr[num2], arr[num1]];  // 구조 분해 할당으로 값 교환
    return arr.join('');  
}
