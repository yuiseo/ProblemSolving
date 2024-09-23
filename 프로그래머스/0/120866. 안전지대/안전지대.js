function solution(board) {
    const n = board.length;
    const visit = new Array(n).fill(0).map(() => new Array(n).fill(0)); // 방문 배열 초기화
    let answer = 0;

    // 상, 하, 좌, 우, 상좌, 상우, 하좌, 하우
    const directy = [-1, 1, 0, 0, -1, -1, 1, 1];
    const directx = [0, 0, -1, 1, -1, 1, -1, 1];

    // 위험 지역 마킹
    function bfs(y, x) {
        const queue = [[y, x]];
        visit[y][x] = 1; // 지뢰 위치 방문 처리

        // 인접한 칸 탐색
        for (let k = 0; k < 8; k++) {
            const dy = y + directy[k];
            const dx = x + directx[k];

            // 경계 조건 확인
            if (dy >= 0 && dy < n && dx >= 0 && dx < n) {
                visit[dy][dx] = 1; // 인접한 칸 방문 처리
            }
        }
    }

    // 모든 지뢰 위치에서 위험 지역 마킹
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (board[i][j] === 1) {
                bfs(i, j); // 지뢰가 있는 지역에서 BFS 수행
            }
        }
    }

    // 안전 지역의 개수 세기
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (visit[i][j] === 0) {
                answer++; // 안전 지역 카운트
            }
        }
    }

    return answer; // 안전 지역의 개수 반환
}

