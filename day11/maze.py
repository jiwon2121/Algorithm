import sys
sys.stdin = open('./4875_input.txt')

def is_go(n, arr):
    delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 3:
                row = i
                col = j

    st = [[row, col]]

    while st:
        row, col = st[-1]
        arr[row][col] = 1

        for d1, d2 in delta:
            ni = row + d1
            nj = col + d2

            if 0 <= ni < n and 0 <= nj <n:
                if arr[ni][nj] == 2:
                    return 1

                elif arr[ni][nj] == 0:
                    st.append([ni, nj])
                    break

        else:
            st.pop()

    return 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input().strip())) for _ in range(N)]

    result = is_go(N, maze)

    print(f'#{tc} {result}')

