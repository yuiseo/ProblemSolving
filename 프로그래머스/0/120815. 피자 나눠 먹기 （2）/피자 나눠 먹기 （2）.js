function solution(n) {
    var answer = 0;
    // 6과 n의 최소 공배수를 찾아서 그 수를 6으로 나누기
    
    function findLCM (n) {
        let lcm = 1;

        while(true){
          if((lcm % n == 0) && (lcm % 6 == 0)){
            break;
          }
          lcm++;
        }
        return lcm
    }
    
    answer = findLCM(n)/6
    
    return answer;
}