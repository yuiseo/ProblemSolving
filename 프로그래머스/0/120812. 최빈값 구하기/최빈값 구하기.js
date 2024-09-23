function solution(array) {
    var answer = 0;
    const dictionary = {}
    
    array.forEach((item)=>{
        if(item in dictionary){
            dictionary[item] +=1
        } else {
            dictionary[item] = 1
        }
    })
    
    // 최대값 찾기
    const values = Object.values(dictionary);
    const maxValue = Math.max(...values);

    // 최대값을 가진 키들 찾기
    const keysWithMaxValue = Object.entries(dictionary)
        .filter(([key, value]) => value === maxValue)
        .map(([key]) => key);

    answer = keysWithMaxValue.length > 1 ? -1 : parseInt(keysWithMaxValue[0]);
    
    
    return answer;
}