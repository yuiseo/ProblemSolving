function solution(n, words) {
    for(let i=1; i<words.length; i++){
        // 끝말 잇기가 틀린 경우
        if(words[i-1].substr(-1)!==words[i][0]){
            return [i%n+1, Math.ceil((i+1)/n)]
        } else{
            // 중복 체크
            for(let j=0; j<i; j++){
                if(words[i] === words[j]) return [i%n+1, Math.ceil((i+1)/n)]
            }
        }
    }
    // 끝말잇기 성공
    return [0,0]
}