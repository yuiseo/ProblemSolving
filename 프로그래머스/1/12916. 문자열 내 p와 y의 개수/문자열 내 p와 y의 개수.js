function solution(s){
    var answer = true;
    
    let count_p = 0
    let count_y = 0
    
    s = s.toLowerCase()
    for(let i=0; i<s.length;i++){
        if(s[i] === 'p'){
            count_p+=1
        } else if (s[i] === 'y') {
            count_y+=1
        }
    }
    
    if(count_p !== count_y){
        return false
    }
    return answer;
}