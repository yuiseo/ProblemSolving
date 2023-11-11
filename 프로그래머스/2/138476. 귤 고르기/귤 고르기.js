function solution(k, tangerine) {
    var answer = 0;
    
    let obj = {}
    
    // object에 크기별 개수 저장
    tangerine.forEach((item)=>{
        obj[item] = ++obj[item] || 1        
    })
    
    // object의 개수 내림차순 
    const sortedObj = Object.values(obj).sort((x,y)=>y-x)
    
    // 가지 수 저장
    let cnt = 0
    
    for(let num of sortedObj){
        ++answer
        cnt += num
        
        // k개 보다 많으면 멈춤
        if(k<=cnt){
            break
        }
    }

    return answer;
}