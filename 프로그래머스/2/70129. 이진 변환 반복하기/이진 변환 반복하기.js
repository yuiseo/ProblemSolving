function solution(s) {
    
    let zero = 0
    let cnt = 0
    
    let len = 0
    while(s.length>1){
        len = s.length
        s = s.split('0').join('')
        
        cnt ++
        zero += (len-s.length)
        
        s = s.length.toString(2)
    }
    
    return [cnt, zero]

}