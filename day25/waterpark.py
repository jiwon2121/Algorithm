import sys
sys.stdin = open('./sample_input.txt')

from collections import deque

del1 = [0, 1, 0, -1]
del2 = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    total = 0
    que = deque()
    visited = [[None for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j, ele in enumerate(input()):
            if ele == 'W':
                que.append((i, j))
                visited[i][j] = 0

    while que:
        row, col = que.popleft()
        for n in range(4):
            ni = row + del1[n]
            nj = col + del2[n]
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == None:
                visited[ni][nj] = visited[row][col] + 1
                que.append((ni, nj))

    for row in visited:
        total += sum(row)

    print(f'#{tc} {total}')
