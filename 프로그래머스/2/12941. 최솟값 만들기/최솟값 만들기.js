function solution(A,B){
    var answer = 0;
    
    //A 오름차순 B 내림차순
    const sortingA = A.sort((a,b)=>a-b)
    const sortingB = B.sort((a,b)=>b-a)
    
    for(var i=0; i<sortingA.length; i++){
        answer+=(sortingA[i]*sortingB[i])
    }
    
    return answer;
}