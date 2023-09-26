import sys
sys.stdin = open('./5188_input.txt')

def go(si = 0, sj = 0, total = 0):
    global min_sum
    total += array[si][sj]

    if si == N-1 and sj == N-1:
        min_sum = min(total, min_sum)
        return

    for d1, d2 in delta:
        ni = si + d1
        nj = sj + d2
        if 0 <= ni < N and 0 <= nj < N:
            if total + array[ni][nj] > min_sum:
                continue
            go(ni, nj, total)

    return


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    array = [list(map(int, input().split())) for _ in range(N)]
    min_sum = 10000
    delta = [[1, 0], [0, 1]]
    go()
    print(f'#{tc} {min_sum}')