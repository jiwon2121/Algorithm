import sys

sys.stdin = open('./input2.txt')

def maze(arr):
    for i in range(100):
        for j in range(100):
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
            if 0 <= ni < 100 and 0 <= nj < 100:
                if arr[ni][nj] == 0:
                    que.append([ni, nj])
                    arr[ni][nj] = 1


                elif arr[ni][nj] == 2:
                    return 1

    return 0


for _ in range(10):
    tc = input()
    array = [list(map(int, input())) for _ in range(100)]

    print(f'#{tc} {maze(array)}')