import sys
sys.stdin = open('./sample_input2.txt')

from collections import deque

connect_dict = {
    1 : [[1, 0], [0, 1], [-1, 0], [0, -1]],
    2 : [[1, 0], [-1, 0]],
    3 : [[0, 1], [0, -1]],
    4 : [[1, 0], [0, -1]],
    5 : [[0, -1], [-1, 0]],
    6 : [[-1, 0], [0, 1]],
    7 : [[1, 0], [0, 1]]
}

delta_dict = {
    1 : [[1, 0], [0, 1], [-1, 0], [0, -1]],
    2 : [[1, 0], [-1, 0]],
    3 : [[0, 1], [0, -1]],
    4 : [[-1, 0], [0, 1]],
    5 : [[0, 1], [1, 0]],
    6 : [[1, 0], [0, -1]],
    7 : [[-1, 0], [0, -1]]
}

T = int(input())
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    que = deque()

    if array[R][C]:
        que.append((R, C))
        visited[R][C] = 1
        cnt = 1

    while que:
        i, j = que.popleft()

        for d1, d2 in delta_dict[array[i][j]]:
            ni = i + d1
            nj = j + d2

            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and array[ni][nj] and [d1, d2] in connect_dict[array[ni][nj]]:
                visited[ni][nj] = visited[i][j] + 1
                if visited[ni][nj] <= L:
                    que.append((ni, nj))
                    cnt += 1


    print(f'#{tc} {cnt}')