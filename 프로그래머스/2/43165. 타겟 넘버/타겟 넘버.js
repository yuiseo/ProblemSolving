let count = 0

function DFS(numbers, target, depth, total){
    if(depth === numbers.length){
        if(total === target){
            count = count+1  
        }
        return
    }
    
    DFS(numbers, target, depth+1, total+numbers[depth])
    DFS(numbers, target, depth+1, total-numbers[depth])
    
}

function solution(numbers, target) {
    DFS(numbers, target,0,0)
    return count;
}