function solution(babbling) {
    var answer = 0;
    
    const possible_babbling = ["aya", "ye", "woo", "ma"]
    
    babbling.forEach((babb) => {
        let target = babb;
        possible_babbling.forEach((pbabb) => {
            if(target.includes(pbabb)){
                target = target.replace(pbabb, 'x');
            }
        });
        
        target = target.replace(/x/gi, '');
        if(target.length === 0) answer += 1;
    });
    
    return answer;
}
