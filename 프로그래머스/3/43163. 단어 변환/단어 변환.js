/**
* 필요한 것
* - 현재 단어와 words의 단어중 하나만 다른 거 찾는 함수
* - 이 목록을 들고 있어야 함.

* - 모든 words를 계속 탐색해야 함..
* - 종료 조건은 완전 같은 단어를 찾았을 때.
* - 최단 거리(?)를 구해야 하는 것으로 보임 => BFS
* - 재방문 x
*/

function diffOneWordExp(str, words, depth){
    let diffOneWords = []
    words.forEach((word)=>{
        let count = 0
        for(let i=0; i < word.length; i++){
            if(word[i]!==str[i]){
                count+=1
            }    
        }
        if(count === 1){
            diffOneWords.push({word,depth:depth+1})
        }
    })
    
    return diffOneWords
}

function BFS(begin, target, words, visited, depth){
    let queue = [{ word: begin, depth: depth }]
    visited.add(begin)
    
    while(queue.length>0){
        current = queue.shift()
        
        if (current.word === target){
            return current.depth
        }
            
        nextLists = diffOneWordExp(current.word, words, current.depth)
        for (const nextList of nextLists) {
            if (visited.has(nextList.word)) continue;
            visited.add(nextList.word);
            queue.push({ word: nextList.word, depth: nextList.depth });
        }
    }
    return depth
    
}


function solution(begin, target, words) {
    var answer = 0;
    let visited = new Set()
    
    // 단어 목록에 target 존재하는지 확인
    if(!words.includes(target)){
        return answer
    }
    
    answer = BFS(begin, target, words, visited,answer)
    
    return answer;
}