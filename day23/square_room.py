import sys
sys.stdin = open('./input2.txt')

def go():
    visited = [[0 for _ in range(N)] for _ in range(N)]
    max_move = 0
    max_num = 0
    que = []

    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                continue

            move = 0
            root = array[i][j]
            visited[i][j] = 1
            que.append([i, j])

            while que:
                ci, cj = que.pop(0)
                num = array[ci][cj]

                if num in memo:
                    move += memo[num]
                    break

                move += 1
                for d1, d2 in delta:
                    ni = ci + d1
                    nj = cj + d2
                    if 0 <= ni < N and 0 <= nj < N and num + 1 == array[ni][nj]:
                        que.append([ni, nj])
                        visited[ni][nj] = 1

            memo[root] = move
            if max_move < move:
                max_move = move
                max_num = root

            elif max_move == move:
                max_num = min(max_num, root)

    return max_num, max_move


T = int(input())
delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]
for tc in range(1, T + 1):
    N = int(input())
    array = [list(map(int, input().split())) for _ in range(N)]
    memo = {}
    ans1, ans2 = go()

    print(f'#{tc} {ans1} {ans2}')
