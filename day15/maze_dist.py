import sys

sys.stdin = open('./5105_input.txt')

def maze(n, arr):
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 3:
                row = i
                col = j

    que = []
    que.append([row, col])
    arr[row][col] = -1
    delta = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    while que:
        row, col = que.pop(0)
        dist = arr[row][col]
        for i, j in delta:
            ni = row + i
            nj = col + j
            if 0 <= ni < n and 0 <= nj < n:
                if arr[ni][nj] == 0:
                    que.append([ni, nj])
                    arr[ni][nj] = dist - 1


                elif arr[ni][nj] == 2:
                    return dist * (-1) - 1

    return 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    array = [list(map(int, input())) for _ in range(N)]

    print(f'#{tc} {maze(N, array)}')