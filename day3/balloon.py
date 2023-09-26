import sys

def pang(n, m, arr):
    max_count = 0
    delta1 = [-1, 0, 1, 0]
    delta2 = [0, 1, 0, -1]

    for i in range(n):
        for j in range(m):
            count = 0
            count += arr[i][j]

            for d1, d2 in zip(delta1, delta2):
                ni = i + d1
                nj = j + d2
                if (0 <= ni < n) and (0 <= nj <m):
                    count += arr[ni][nj]

            if max_count < count:
                max_count = count

    return max_count


sys.stdin = open('./input4.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(N)]

    result = pang(N, M, array)

    print(f'#{tc} {result}')