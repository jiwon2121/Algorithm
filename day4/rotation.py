import sys


def rotation(n,arr):
    arr_90 = [['' for _ in range(n)] for _ in range(n)]
    # 90도
    for i in range(n):
        for j in range(n):
            arr_90[i][j] += arr[n - 1 - j][i]

    return arr_90


sys.stdin = open('./input5.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    array = [input().split() for _ in range(N)]

    r_90 = rotation(N, array)
    r_180 = rotation(N, r_90)
    r_270 = rotation(N, r_180)

    print(f'#{tc}')
    for i in range(N):
        print(*r_90[i], sep='', end = ' ')
        print(*r_180[i], sep='', end = ' ')
        print(*r_270[i], sep='')