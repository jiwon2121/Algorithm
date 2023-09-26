import sys

sys.stdin = open('./input1.txt')

def maze(arr):
    for i in range(16):
        for j in range(16):
            if arr[i][j] == 3:
                row = i
                col = j

    que = []
    que.append([row, col])
    arr[row][col] = 1
    delta = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    while que:
        row, col = que.pop(0)
        for i, j in delta:
            ni = row + i
            nj = col + j
            if 0 <= ni < 16 and 0 <= nj < 16:
                if arr[ni][nj] == 0:
                    que.append([ni, nj])
                    arr[ni][nj] = 1


                elif arr[ni][nj] == 2:
                    return 1

    return 0


for _ in range(10):
    tc = input()
    array = [list(map(int, input())) for _ in range(16)]

    print(f'#{tc} {maze(array)}')
