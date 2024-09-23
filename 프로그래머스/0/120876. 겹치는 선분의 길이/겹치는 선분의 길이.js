function solution(lines) {
    // 선분의 시작과 끝 사이의 각 좌표가 포함된 선분의 수를 기록할 배열
    const lineMap = new Array(201).fill(0); // -100 ~ 100을 다루기 위해 201칸 배열을 사용

    // 각 선분의 시작점과 끝점 사이의 구간을 lineMap에 표시
    lines.forEach(([start, end]) => {
        for (let i = start; i < end; i++) {
            lineMap[i + 100]++; // 음수를 처리하기 위해 +100을 더함
        }
    });
    

    // 겹친 부분이 2개 이상인 구간의 길이를 구함
    let answer = 0;
    lineMap.forEach(count => {
        if (count >= 2) {
            answer++;
        }
    });

    return answer;
}
