function  BFS(n, start,visited, computers, count){
    const queue = [start]
    visited[start] = count
    
    while(queue.length>0){
        const cur = queue.shift()
        
        for(let i=0;i<n;i++){
            if(computers[cur][i] === 1 && visited[i] === 0){
                queue.push(i)
                visited[i] = count
            }
        }
    } 
}

function solution(n, computers) {
    var answer = 0;
    const visited = Array(n).fill(0)  
    
    for(let i=0;i<n;i++){
        if(visited[i] === 0){
            answer+=1;
            BFS(n, i, visited, computers, answer)
        }
    }
    return answer;
}