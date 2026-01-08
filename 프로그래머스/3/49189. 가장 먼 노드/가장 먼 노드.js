function howFarStartNode(n, nodeMap){
    const visited = Array(n+1).fill(-1)
    let queue = [1]
    let dist = 0
    let count = 0
    visited[1] = dist
    
    while(queue.length>0){
        // 일단은 queue를 for문을 돌려.
        // for문으로 뺀 값을 key로 해서 value를 가져와.
        // 거기에서 방문 안한애를 queue에 넣어
        // 그리고 이 for문이 끝나면 dist++
        let nextValues = []
        dist++
        
        for (const q of queue) {
            const arr = nodeMap.get(q)
            for (const a of arr) {
                if (visited[a] < 0) {
                    visited[a] = dist
                    nextValues.push(a)
                }
            }
        }
        
        queue = nextValues  
    }
    
    
    for (const v of visited) {
        if (v === dist-1) {
            count+=1
        }
    }
    
    return count
}
function solution(n, edge) {
    var answer = 0;
    const nodeMap = new Map()
    const startNode = 1

    for(const e of edge){
        const [start ,end] = e
        if (!nodeMap.has(start)) nodeMap.set(start, new Set())
        if (!nodeMap.has(end)) nodeMap.set(end, new Set())

        nodeMap.get(start).add(end)
        nodeMap.get(end).add(start)
    }
    answer = howFarStartNode(n, nodeMap)
    
    return answer;
}