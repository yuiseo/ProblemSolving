function solution(rsp) {
    var answer = '';
    
    [...rsp].map((item)=>{
        switch(item){
            case "2":
                answer +='0'
                break
            case "0":
                answer += '5'
                break
            default:
                answer+='2'
                break
        }
    })
    return answer;
}