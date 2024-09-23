function solution(numer1, denom1, numer2, denom2) {
    var answer = [];
    const denom3 = denom1*denom2
    const numer3 = numer1*denom2 + numer2*denom1
    console.log(denom3, numer3)
    
    function gcd (a,b) {
        const find = a % b
        if(find===0){return b}else{return gcd(b,find)}
    }
    
    const gcd_value = gcd(numer3, denom3)
    answer = [numer3/gcd_value, denom3/gcd_value]
    return answer;
}