function solution(n) {
    var answer = 0;
    
    let target=1
    while(true){
        if(target === n){
            answer+=1
            break
        }
        
        if(n%target ===0){
            answer+=1
            target+=1
        } else {
            target+=1
        }
        
    }
    return answer;
}