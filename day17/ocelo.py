import sys
sys.stdin = open('./sample_input(1).txt')


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [[0 for _ in range(N)] for _ in range(N)]
    board[N // 2][N // 2] = 2
    board[N // 2 - 1][N // 2 - 1] = 2
    board[N // 2][N // 2 - 1] = 1
    board[N // 2 - 1][N // 2] = 1

    for _ in range(M):
        i, j, stone = map(int, input().split())
        i -= 1
        j -= 1
        board[i][j] = stone

        for d1, d2 in [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, -1], [-1, 1], [1, -1]]:
            end = [i, j]
            ni = d1 + i
            nj = d2 + j

            while 0 <= ni < N and 0 <= nj < N:
                if board[ni][nj] == 0:
                    break
                elif board[ni][nj] == stone:
                    end = [ni, nj]
                    break
                ni += d1
                nj += d2

            ni = i
            nj = j
            while end != [ni, nj]:
                board[ni][nj] = stone
                ni += d1
                nj += d2

    black = 0
    white = 0
    for row in board:
        for ele in row:
            if ele == 1:
                black += 1
            elif ele == 2:
                white += 1

    print(f'#{tc} {black} {white}')