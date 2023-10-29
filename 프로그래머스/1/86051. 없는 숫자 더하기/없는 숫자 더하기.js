function solution(numbers) {
    var answer = 0;
    
    let list = [0,0,0,0,0,0,0,0,0,0]

    
    numbers.map((item)=>list[item] = 1)
    
    list.map((item,idx)=>{
        if(item === 0) {
            answer+=idx
        }
    } )
    
    
    return answer;
}